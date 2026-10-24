# Contributing to Open Detection Engineering

ODE is intended to be built and maintained by the Detection Engineering community. Contributions of all sizes are welcome.

## Ways to Contribute

You can contribute by:
- correcting technical errors
- improving existing lessons
- reviewing curriculum
- proposing new modules
- writing lessons
- developing labs
- contributing datasets
- contributing platform-specific examples
- improving documentation
- participating in curriculum discussions

## Small Changes

Corrections, clarifications, examples, and other limited changes may be submitted directly as pull requests.

## Large Changes

Please open an issue before beginning substantial work such as:
- new Core modules
- new tracks
- major restructuring
- large labs
- new datasets
- major changes to established guidance

This allows contributors and maintainers to discuss the direction before significant work is completed.

## Technical Expectations

Contributions should be:
- technically accurate
- practical
- evidence based where appropriate
- vendor neutral when part of Core
- clearly written
- original or appropriately licensed
- suitable for professional education

Platform tracks may discuss specific products in depth. Marketing material and unsupported vendor claims are not appropriate.

## Review

Content may be reviewed for:
- technical accuracy
- operational realism
- clarity
- instructional quality
- licensing
- consistency with the surrounding curriculum

Maintainers may request additional review from relevant subject-matter experts.

## Attribution

Accepted contributors will be credited through Git history and may also be included in project contributor or lesson metadata.

## AI-Assisted Contributions

ODE exists to capture and share the knowledge, judgment, and experience of practitioners. Contributors may use AI tools as part of their writing, research, editing, or development workflow, but AI does not replace contributor responsibility or subject-matter expertise.

Contributors are responsible for all material they submit, regardless of how it was produced.

Contributors are expected to:

- understand and be able to explain every technical claim they submit
- verify technical details, examples, references, queries, code, and detection logic
- apply their own subject-matter judgment to the material
- ensure that examples and recommendations reflect defensible engineering practices
- review AI-assisted output for inaccuracies, unsupported claims, fabricated references, and misleading generalizations
- substantially contribute the expertise, analysis, or practical insight represented by the submission

AI tools may be used for activities such as drafting, editing, restructuring, brainstorming, code assistance, research support, or generating initial examples. However, contributors must validate the resulting material before submission.

ODE does not accept content that substitutes generated output for practitioner knowledge. Examples include:

- technically shallow material submitted without meaningful expert review
- fabricated or unverifiable technical claims or references
- generic lessons that do not demonstrate understanding of the subject
- generated detection logic, queries, code, or labs that the contributor has not tested or validated
- bulk-generated content submitted primarily to increase contribution volume

Maintainers evaluate contributions based on technical quality, accuracy, originality of insight, usefulness to practitioners, and the contributor's demonstrated understanding of the material.

The use of AI alone is not grounds for rejection. Poorly validated, technically weak, misleading, or low-effort contributions are.

## Developer Certificate of Origin

ODE uses the Developer Certificate of Origin (DCO) instead of a contributor license agreement. Every commit must be signed off, which certifies the statements below.

Sign off by adding `-s` to your commit:

```bash
git commit -s -m "Fix Sysmon event ID in telemetry lesson"
```

This appends a line to your commit message:

```text
Signed-off-by: Your Name <your.email@example.com>
```

If you forget, amend with `git commit --amend -s` (or `git rebase --signoff` for several commits) and force-push your branch. A bot checks every pull request.

> Developer Certificate of Origin, Version 1.1
>
> By making a contribution to this project, I certify that:
>
> (a) The contribution was created in whole or in part by me and I have the right to submit it under the open source license indicated in the file; or
>
> (b) The contribution is based upon previous work that, to the best of my knowledge, is covered under an appropriate open source license and I have the right under that license to submit that work with modifications, whether created in whole or in part by me, under the same open source license (unless I am permitted to submit under a different license), as indicated in the file; or
>
> (c) The contribution was provided directly to me by some other person who certified (a), (b) or (c) and I have not modified it.
>
> (d) I understand and agree that this project and the contribution are public and that a record of the contribution (including all personal information I submit with it, including my sign-off) is maintained indefinitely and may be redistributed consistent with this project or the open source license(s) involved.

For ODE, "the license indicated" is the license for the relevant part of the project, as described in [LICENSE.md](LICENSE.md).

## Contributor Responsibility

By submitting a contribution, you also confirm that:
- It does not knowingly contain confidential, employer-owned, or improperly licensed material.
- You have disclosed any relevant affiliation (see the pull request template).

## Questions and Discussion

Use [GitHub Discussions](https://github.com/HardCounterIO/ode/discussions) for questions, early ideas, and open-ended curriculum conversation. Open an issue once an idea is a concrete proposal (a new module, lab, dataset, or correction) using the matching issue template.

The [ODE Discord](https://discord.gg/aBW2dwhpT9) is available for quick questions, real-time chat, and coordinating with other contributors. Decisions about the curriculum are made on GitHub. If something is agreed in Discord, record it in the relevant issue, discussion, or pull request.

To report a security problem or accidentally committed sensitive data, follow [SECURITY.md](SECURITY.md) instead.
