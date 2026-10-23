---
name: Module Research
about: Use this template to coordinate the research and lesson design for a Core module
  before lesson writing begins.
title: "[RESEARCH] <NN> <Module Name>"
labels: core, research
assignees: ''

---

## Module

Module number and name (e.g. `02 Telemetry & Data`).

Target directory: `core/NN-slug/`

## Purpose

What this module is for and where it sits in the Core sequence.

## Goal of This Issue

Design the module's structure so individual lessons can be claimed and written. This issue does **not** produce lesson content.

Research is complete when a pull request is merged that adds:

- `core/NN-slug/README.md`, based on [`templates/module-template.md`](https://github.com/HardCounterIO/ode/blob/main/templates/module-template.md), containing:
  - module learning objectives
  - prerequisites
  - the proposed lesson list, with for each lesson:
    - 2–4 learning objectives
    - key topics
    - explicitly out of scope
  - a **Boundaries** section describing what this module covers versus adjacent modules
- `core/NN-slug/module-metadata.yml`, based on [`templates/module-metadata.yml`](https://github.com/HardCounterIO/ode/blob/main/templates/module-metadata.yml), with `status: draft`

Once merged, a maintainer opens one issue per lesson as a sub-issue of this one.

## Inputs

### Community Feedback

Feedback from curriculum discussions that should be addressed in this module. Link the original comments.

- 

### Seed Material

Existing material to use as a starting point. Seed material is an input to evaluate, not a finished structure.

- 

### References

Standards, frameworks, research, or other references relevant to this module.

- 

## Known Overlaps

Topics that touch adjacent modules and need an agreed boundary.

| Topic | This module | Other module(s) |
|---|---|---|
|  |  |  |

## How to Participate

- **Claim:** comment on this issue to join. A maintainer will assign you and add you to the Contributors section below. Multiple contributors may claim the same research issue.
- **Lead:** a maintainer designates one contributor as lead. The lead coordinates, keeps work moving, and opens the pull request. The lead does not make every decision alone.
- **Suggest inputs:** only maintainers can edit this issue, so post feedback, seed material, references, or overlaps as comments and a maintainer will add them above.
- **Collaborate:** use this issue to coordinate. The lead forks the repository and opens a draft pull request early so everyone works from the same document. To let co-contributors push to that branch, the lead adds them as collaborators on their fork (fork **Settings → Collaborators**). Contributors who are not added can propose edits with suggested changes in the pull request review. Every commit must be signed off ([DCO](https://github.com/HardCounterIO/ode/blob/main/CONTRIBUTING.md#developer-certificate-of-origin)).
- **Boundary review:** before merging, a contributor from each adjacent module, or a maintainer, confirms the Boundaries section.
- **Inactivity:** claims with no activity for 4 weeks may be released after a reminder.

## Contributors

Lead:

Contributors:

## Additional Context

Anything else relevant to the research for this module?
