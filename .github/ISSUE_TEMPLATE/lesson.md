---
name: Lesson
about: Use this template to coordinate writing one lesson of a Core module after the
  module's research is merged.
title: "[LESSON] <NN>.<N> <Lesson Title>"
labels: core, new-content
assignees: ''

---

## Lesson

Module: `NN Module Name`

Lesson: `N. Lesson Title`

Target file: `core/NN-slug/NN-lesson-slug.md`

Research issue: #

## Scope

Copied from the module README, which is the source of truth. If the scope needs to change while writing, change the README in the same pull request and say why.

### Learning Objectives

- 

### Key Topics

- 

### Out of Scope

- 

## Goal of This Issue

Write the lesson. The lesson is complete when a pull request is merged that:

- adds the target file, based on [`templates/lesson-template.md`](https://github.com/HardCounterIO/ode/blob/main/templates/lesson-template.md) and written to the [Style Guide](https://github.com/HardCounterIO/ode/blob/main/docs/STYLE-GUIDE.md)
- meets each learning objective above and stays out of the out-of-scope topics, pointing to the lesson or module that covers them instead
- passes the [checklist for authors](https://github.com/HardCounterIO/ode/blob/main/docs/STYLE-GUIDE.md#9-checklist-for-authors)
- links the lesson from the module README's lesson list
- updates the module's `ai_assistance` field and README **AI Assistance** section to cover this lesson

The module's `status` stays `draft`. Technical review happens at the module level once its lessons are written ([Review Process](https://github.com/HardCounterIO/ode/blob/main/docs/REVIEW-PROCESS.md#6-process)).

## How to Participate

- **Claim:** comment on this issue to take it. A maintainer will assign you and add you to the Contributors section below. One writer leads each lesson; others are welcome to contribute.
- **Collaborate:** open a draft pull request early and link this issue. To let co-contributors push to your branch, add them as collaborators on your fork (fork **Settings → Collaborators**). Every commit must be signed off ([DCO](https://github.com/HardCounterIO/ode/blob/main/CONTRIBUTING.md#developer-certificate-of-origin)).
- **Boundaries:** if the lesson starts covering material owned by another lesson or module, raise it here or in the pull request rather than expanding the scope.
- **Inactivity:** claims with no activity for 4 weeks may be released after a reminder.

## Contributors

Writer:

Contributors:

## Additional Context

Anything else relevant to writing this lesson?
