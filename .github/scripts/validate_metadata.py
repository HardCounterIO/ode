#!/usr/bin/env python3
"""Validate module-metadata.yml files against docs/REVIEW-PROCESS.md.

Errors fail the check. Review expiry only warns, so one stale module does not
block unrelated pull requests.
"""

import datetime
import pathlib
import re
import sys

import yaml

STATUSES = {"draft", "in-review", "reviewed", "stable", "needs-update", "deprecated"}
REVIEWED_STATUSES = {"reviewed", "stable"}
STRING_FIELDS = ["title", "slug", "summary", "ai_assistance"]
LIST_FIELDS = [
    "learning_objectives",
    "prerequisites",
    "authors",
    "reviewers",
    "maintainers",
    "related_tracks",
    "related_labs",
    "related_datasets",
]
REQUIRED = STRING_FIELDS + LIST_FIELDS + ["status", "version", "last_reviewed"]
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
EXPIRY_DAYS = 365

errors = 0


def error(path, message):
    global errors
    errors += 1
    print(f"::error file={path}::{message}")


def warning(path, message):
    print(f"::warning file={path}::{message}")


def load(path):
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        error(path, f"invalid YAML: {exc}")
        return None
    if not isinstance(data, dict):
        error(path, "top level must be a mapping")
        return None
    return data


def handle(value):
    return str(value).strip().lstrip("@").lower()


def parse_date(value):
    if isinstance(value, datetime.date):
        return value
    if isinstance(value, str) and DATE_RE.match(value):
        try:
            return datetime.date.fromisoformat(value)
        except ValueError:
            return None
    return None


def check_template(path):
    data = load(path)
    if data is None:
        return
    for key in REQUIRED:
        if key not in data:
            error(path, f"template is missing field '{key}'")


def check_module(path):
    data = load(path)
    if data is None:
        return

    for key in REQUIRED:
        if key not in data:
            error(path, f"missing required field '{key}'")
    for key in data:
        if key not in REQUIRED:
            warning(path, f"unknown field '{key}'")

    for key in STRING_FIELDS:
        value = data.get(key)
        if key in data and not (isinstance(value, str) and value.strip()):
            error(path, f"'{key}' must be a non-empty string")

    for key in LIST_FIELDS:
        value = data.get(key)
        if key not in data:
            continue
        if not isinstance(value, list):
            error(path, f"'{key}' must be a list")
            continue
        for item in value:
            if not (isinstance(item, str) and item.strip()):
                error(path, f"'{key}' contains an empty entry (unfilled template?)")
                break

    if isinstance(data.get("learning_objectives"), list) and not data["learning_objectives"]:
        error(path, "'learning_objectives' must have at least one entry")

    slug = data.get("slug")
    if isinstance(slug, str) and slug.strip():
        if not SLUG_RE.match(slug):
            error(path, f"slug '{slug}' must be lowercase kebab-case")
        directory = re.sub(r"^\d+-", "", path.parent.name)
        if directory != slug:
            error(path, f"slug '{slug}' must match the directory name '{path.parent.name}' without its number prefix")

    version = data.get("version")
    if "version" in data and (version is None or not str(version).strip()):
        error(path, "'version' must not be empty")

    status = data.get("status")
    if "status" in data and status not in STATUSES:
        error(path, f"status '{status}' must be one of: {', '.join(sorted(STATUSES))}")

    last_reviewed = data.get("last_reviewed")
    reviewed_on = None
    if last_reviewed is not None:
        reviewed_on = parse_date(last_reviewed)
        if reviewed_on is None:
            error(path, "'last_reviewed' must be null or a YYYY-MM-DD date")
        elif reviewed_on > datetime.date.today():
            error(path, "'last_reviewed' is in the future")

    reviewers = data.get("reviewers") if isinstance(data.get("reviewers"), list) else []
    authors = data.get("authors") if isinstance(data.get("authors"), list) else []

    overlap = {handle(r) for r in reviewers} & {handle(a) for a in authors}
    if overlap:
        error(path, f"reviewers must be independent of authors (both: {', '.join(sorted(overlap))})")

    if status in REVIEWED_STATUSES:
        if not reviewers:
            error(path, f"status '{status}' requires at least one reviewer")
        if last_reviewed is None:
            error(path, f"status '{status}' requires 'last_reviewed'")
        elif reviewed_on is not None:
            age = (datetime.date.today() - reviewed_on).days
            if age > EXPIRY_DAYS:
                warning(path, f"last reviewed {age} days ago; past the {EXPIRY_DAYS}-day expiry, so the status should be 'needs-update'")


def main():
    root = pathlib.Path(".")
    template = root / "templates" / "module-metadata.yml"
    if template.exists():
        check_template(template)

    modules = sorted(
        p
        for p in root.rglob("module-metadata.yml")
        if ".git" not in p.parts and "templates" not in p.parts
    )
    for path in modules:
        check_module(path)

    print(f"Checked {len(modules)} module(s); {errors} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
