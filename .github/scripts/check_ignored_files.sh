#!/usr/bin/env bash
# Fail if any tracked file matches a .gitignore rule (i.e. it was force-added).
# This covers AI-tool files, secrets, binaries, and anything else .gitignore
# keeps out. Deliberate exceptions go in .github/ignored-file-exceptions.txt.
set -euo pipefail

exceptions=".github/ignored-file-exceptions.txt"

found="$(git ls-files -ci --exclude-standard)"

if [ -f "$exceptions" ]; then
  allowed="$(grep -vE '^[[:space:]]*(#|$)' "$exceptions" || true)"
  if [ -n "$allowed" ]; then
    found="$(grep -vxFf <(printf '%s\n' "$allowed") <<<"$found" || true)"
  fi
fi

if [ -n "$found" ]; then
  while IFS= read -r file; do
    echo "::error file=${file}::Tracked file matches .gitignore. Remove it from the PR (git rm --cached), or add it to ${exceptions} if it is deliberate and reviewed."
  done <<<"$found"
  exit 1
fi

echo "No tracked files match .gitignore."
