# Review Process

This document defines what it means for ODE content to be "reviewed," who can review it, and how review status is recorded. It makes concrete the review expectations in [CONTRIBUTING.md](../CONTRIBUTING.md#review) and implements the technical review standards called for in the [roadmap](../ROADMAP.md).

## 1. Current Configuration

These values are the current settings. They may be changed through the process in section 12, and this table is updated when they do.

| Setting | Current value |
|---|---|
| Approving reviewers required for `reviewed` | 1 |
| Reviewer must be independent of the author | Yes |
| Author may count as their own reviewer | No |
| Review expiry | 12 months after `last_reviewed` |
| Who may set `status` to `reviewed` or `stable` | Maintainers |

The reviewer requirement is expected to rise to 2 once there are enough active reviewers to support it.

## 2. Status Lifecycle

Each module records its state in `module-metadata.yml`. Allowed `status` values:

| Status | Meaning |
|---|---|
| `draft` | Being written. Makes no claim about accuracy. |
| `in-review` | Complete enough to review, and a review request is open. |
| `reviewed` | Passed review by the required number of independent reviewers. |
| `stable` | Reviewed, and every example (queries, rules, code) has been executed and validated. Used as the reference version in labs. |
| `needs-update` | Past its review date, or a valid correction is open. |
| `deprecated` | Superseded or no longer recommended. Kept for reference with a pointer to the replacement. |

Transitions:

```text
draft → in-review → reviewed → stable
          ↑            │          │
          └────────────┴──────────┘  (re-review after changes)
reviewed / stable → needs-update   (expiry, or a valid correction)
any status → deprecated
```

A significant change to a `reviewed` or `stable` module returns it to `in-review`. A typo or clarification does not.

## 3. Roles

- **Author**: wrote the content.
- **Reviewer**: someone other than the author who evaluates the content and records an approval. Reviewers are listed in [MAINTAINERS.md](../MAINTAINERS.md) or, for one-off review, recorded in the PR.
- **Maintainer**: merges, and sets `status` after verifying the approvals.

### Independence

A reviewer counts toward the requirement only if they:

- are not the author or a co-author,
- have disclosed any affiliation relevant to the content ([affiliation disclosure](../MAINTAINERS.md#affiliation-disclosure)), and
- have no commercial interest in a product the content materially concerns.

For vendor-specific content (platform tracks), at least one reviewer should be independent of that vendor where practical ([GOVERNANCE.md](../GOVERNANCE.md#commercial-organizations)).

### Bootstrap rule

While the project has only the Project Lead:

- The Project Lead may approve and merge governance, documentation, templates, tooling, and other non-curriculum changes.
- Curriculum content authored by the Project Lead may be merged as `draft` or `in-review`, and **may not become `reviewed` or `stable` without an independent reviewer's approval.** Self-review cannot establish technical correctness, and ODE's value rests on practitioner review.
- Content from other contributors may be reviewed and approved by the Project Lead until additional reviewers exist, provided the Project Lead has no conflict with it.

This rule ends when the project has enough reviewers to meet the requirement without it. Until then, published modules should clearly show their status.

## 4. What Review Covers

Reviewers evaluate the following. These match the focus areas in the review request and PR templates.

- **Technical accuracy**: Are the claims correct? Are the references real and do they support the claims?
- **Operational realism**: Would this work in a real environment? Does it account for noise, scale, data quality, cost, and failure modes?
- **Vendor neutrality**: Does Core avoid product assumptions? Is Splunk SPL used as described in the [style guide](STYLE-GUIDE.md#5-example-languages)?
- **Instructional quality**: Are the objectives measurable, the order sensible, and the examples clear?
- **Completeness**: Are important caveats, tradeoffs, and differing viewpoints covered?
- **Licensing and provenance**: Is the work original or properly licensed? Is any third-party material identified?
- **Safety and data hygiene**: Does it follow the example data and attack-simulation rules in the style guide and [SECURITY.md](../SECURITY.md)?

## 5. Reviewer Checklist

Copy this into the review comment.

```markdown
**Reviewer:** @handle
**Affiliation / conflicts:** None | describe
**Scope reviewed:** files or sections

- [ ] Claims are accurate and supported
- [ ] References exist and say what the lesson says they say
- [ ] Detection logic was run against data, not only read
- [ ] False positives, tuning, and evasion are addressed
- [ ] Core content is vendor-neutral (or SPL is used per the style guide)
- [ ] Learning objectives are measurable and met
- [ ] Example data follows the style guide
- [ ] No licensing or provenance concerns
- [ ] Tradeoffs and differing views are represented fairly

**Verdict:** Approve | Request changes | Comment
**Notes:**
```

Reviewers should execute queries and rules where possible. A reviewer who only read the logic should say so, and that review does not count toward `stable`.

## 6. Process

1. **Author** completes the module, runs the author checklist in the [style guide](STYLE-GUIDE.md#9-checklist-for-authors), and opens a pull request. Substantial new modules start with an issue ([CONTRIBUTING.md](../CONTRIBUTING.md#large-changes)).
2. **Author** sets `status: in-review` and opens a **Technical Review Request** issue linking the PR, naming the expertise needed.
3. **Reviewer** completes the checklist and records the verdict as a GitHub PR review.
4. **Author** addresses feedback. Reviewers re-check what changed.
5. **Maintainer** verifies the required independent approvals, then updates `module-metadata.yml` in the same PR:
   - `status`
   - `reviewers`: GitHub handles of approving reviewers
   - `last_reviewed`: the approval date (`YYYY-MM-DD`)
6. **Maintainer** merges.

If a reviewer and author disagree and the difference is a matter of legitimate practitioner opinion, the lesson should present both views with their tradeoffs rather than one side winning. If the disagreement is about fact, resolve it with evidence (a reproducible test or a primary source). Unresolved disputes go to an issue and are decided by the maintainers, publicly, per [GOVERNANCE.md](../GOVERNANCE.md#decisions).

## 7. Corrections

Anyone can report a problem with the Technical Correction issue template. Maintainers triage using the impact selected on the template:

| Impact | Handling |
|---|---|
| Minor clarification | Fix by normal PR. Status unchanged. |
| Technical inaccuracy | Confirm, fix, and have the fix reviewed. Status becomes `in-review` if the change is significant. |
| Could materially mislead learners | Set the module to `needs-update` immediately, fix, and re-review before restoring status. |
| Security-sensitive or operationally significant | Treat as high priority. Set `needs-update` immediately, and follow [SECURITY.md](../SECURITY.md) if sensitive data is involved. |

Record significant corrections in the PR description so the history shows what changed and why.

## 8. Expiry and Periodic Review

Detection knowledge ages quickly: products change, telemetry changes, and techniques evolve.

- A module expires 12 months after `last_reviewed`. On expiry its status becomes `needs-update`.
- Maintainers review the list of expiring modules regularly and open issues for them.
- Re-review confirms the content is still accurate. It does not need to repeat the full process if nothing changed, but the reviewer, `reviewers`, and `last_reviewed` are updated.
- Modules that reference specific product or ATT&CK versions should be checked against newer releases when those ship.

## 9. Labs and Datasets

- Labs and datasets are reviewed with the same independence requirement.
- A dataset review confirms provenance, licensing, absence of real personal or proprietary data ([LICENSE.md](../LICENSE.md#datasets)), and that the intended malicious and benign activity is present as described.
- A lab review means someone other than the author completed it from the instructions, on a clean environment, and reached the stated outcome.

## 10. Releases

Versioned curriculum releases (roadmap Phase 5) include only modules that are `reviewed` or `stable` at release time. Draft and in-review content may be present in the repository but is labeled as such and excluded from the release version.

## 11. Transparency

Review is public. Reviews happen in pull requests and issues, and a module's `reviewers` and `last_reviewed` are visible in its metadata. Reviewers are credited through Git history and project metadata ([CONTRIBUTING.md](../CONTRIBUTING.md#attribution)).

## 12. Changing This Process

Changes to the settings in section 1, to the status definitions, or to the independence rules are governance changes. Propose them in an issue, discuss publicly, and record the outcome here ([GOVERNANCE.md](../GOVERNANCE.md#decisions)).
