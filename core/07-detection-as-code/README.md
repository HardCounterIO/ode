# Detection-as-Code

## Overview

Detection-as-Code covers managing detections the way software is managed: stored in version control, reviewed before they change, validated automatically, and deployed by a repeatable process. Learners will be introduced to what the practice is and when it pays off, repository structure, rule formats and metadata, code review, continuous integration, and automated deployment with the ability to reverse it. Rule examples use Sigma for portable logic and Splunk SPL as the reference query language.

## Learning Objectives

By the end of this module, learners should be able to:

- Justify when managing detections as code is worth its overhead, and identify teams for which it is premature.
- Design a repository layout and metadata schema for a detection set, and defend each required field by the decision it supports.
- Distinguish which validation belongs in a pre-commit hook, which belongs in continuous integration, and which requires a human reviewer.
- Review a detection change against criteria that automation cannot check.
- Build a path that takes a merged change to a running detection, and state how to reverse it.
- Diagnose drift between a detection repository and the platform running the detections, and choose a reconciliation approach.

## Prerequisites

- Module 01: Detection Engineering Foundations
- Module 05: Detection Development
- Module 06: Testing & Validation
- Working knowledge of Git branching, merging, and pull requests
- Ability to read YAML and a continuous integration configuration file

## Lessons

### 1. What Detection-as-Code Means

**Learning Objectives**

- Distinguish detection-as-code from keeping rule files in a repository.
- Justify the overhead against the problems it solves, and identify teams for which it is premature.
- Choose which system holds the authoritative copy of a production detection, and state what that choice costs.

**Key Topics**

- The borrowed practices: version control, peer review, automated validation, repeatable deployment
- What a detection repository holds besides logic
- Costs: tooling, delay, and team skills
- The authoritative source decision: repository, platform, or both kept in sync
- Preconditions for adopting the practice
- Failure modes: a pipeline nobody can debug, and review that becomes a rubber stamp

**Out of scope**

- Introducing detection engineering concepts (Module 01)
- Any specific pipeline implementation (platform tracks)

### 2. Version Control for Detection Content

**Learning Objectives**

- Design a repository layout for a detection set that still works past a few hundred rules.
- Write commits and pull requests that leave a history a reviewer or auditor can read.
- Evaluate strategies for consuming upstream community content without losing local changes.

**Key Topics**

- Layout choices: by purpose, data source, platform, or technique
- Keeping rules, tests, test data, and supporting objects together
- Branching models, and why long-lived branches age badly
- Commit hygiene and the rule diff as the record of change
- Consuming upstream content: forking, vendoring, and overlays
- Retiring a rule without losing its history

**Out of scope**

- Git fundamentals
- The meaning of retired and deprecated states (Module 09)

### 3. Rule Formats and Metadata

**Learning Objectives**

- Compare a portable rule format with a platform-native format, and justify a choice for a given team.
- Specify a metadata schema, justifying each required field by the decision or system it serves.
- Validate a rule set against that schema automatically.

**Key Topics**

- How a portable rule becomes a platform query, and what the conversion does not carry
- Field naming and the dependency on a normalization schema
- Stable identifiers that survive renaming and moving
- Fields downstream systems consume: severity, technique mapping, data source, status, and ownership
- Documentation that travels with the rule: goal, assumptions, blind spots, known benign causes, and response guidance
- Schema enforcement: required fields, allowed values, and naming conventions

**Out of scope**

- Writing the detection logic (Module 05)
- Choosing the severity of a detection (Module 04)
- Lifecycle state semantics (Module 09)
- Conversion tooling and backends (platform tracks)

### 4. Code Review for Detections

**Learning Objectives**

- Review a detection change against criteria that automation cannot check.
- Distinguish review findings that should block a merge from those that should not.
- Design a review routing and ownership model for a detection repository.

**Key Topics**

- What a human reviewer adds: logic against the stated goal, assumptions, and whether a responder can act on the result
- Reviewing a detection you cannot run, and recording that limit
- Ownership and required approvals
- Reviewing emergency changes without discarding the process
- Failure modes: rubber-stamp approval, and arguing over style a linter should settle

**Out of scope**

- Whether the tests in a change are adequate (Module 06)
- Approving a production rollout (Module 08)

### 5. Continuous Integration for Detections

**Learning Objectives**

- Design a continuous integration pipeline for a detection repository with explicit stages and gates.
- Distinguish checks that belong in a pre-commit hook, in continuous integration, or in human review.
- Diagnose whether a failing detection test points to the logic, the test data, or the pipeline.

**Key Topics**

- Stages: formatting and syntax, schema validation, logic validation, and tests against data
- Where test fixtures live, and handling data that is too large or too sensitive to commit
- Gates: what blocks a merge and what only warns
- Pipeline latency and keeping feedback fast
- Failure modes: flaky tests, environment drift, and checks disabled to unblock a release

**Out of scope**

- Designing test cases and judging coverage (Module 06)
- Platform-specific pipeline configuration (platform tracks)

### 6. Automated Deployment and Release

**Learning Objectives**

- Build a path that takes a merged change to a running detection without manual steps.
- Compare deploying by pushing to a platform interface with deploying a packaged content artifact.
- Detect drift between the repository and deployed state, and reverse a change that should not have shipped.

**Key Topics**

- Two deployment shapes: pushing rules to a platform, and installing a versioned package
- Promoting content between development, staging, and production
- Versioning a release and recording what shipped
- Rollback: reverting a commit versus reverting a deployment
- Pipeline credentials and least privilege
- Verifying a deployed rule is present, enabled, running, and matching the repository
- Drift from console edits, and returning them to the repository

**Out of scope**

- Rollout strategy, staged exposure, and tuning a live detection (Module 08)
- Monitoring detection health after deployment (Module 09)

## Boundaries

| Topic | This module | Adjacent module(s) |
| --- | --- | --- |
| The concept | Full treatment | 01 Detection Engineering Foundations (brief introduction) |
| Detection logic | The format and metadata that carry the logic | 05 Detection Development (writing the logic) |
| Severity and priority | That the field exists, is validated, and is consumed | 04 Detection Design (deciding the value) |
| Testing | Running tests automatically as a merge gate | 06 Testing & Validation (what to test, and whether a test is adequate) |
| Deployment | The mechanism from merge to running rule, and reversing it | 08 Deployment, Tuning & Operations (rollout strategy, staged exposure, tuning) |
| Documentation | Where design and response documentation lives, and its metadata | 04 Detection Design (the design document) |
| Metadata and versioning | Schema, validation, and change history | 09 Detection Health & Lifecycle (lifecycle states and review cadence) |
| Pipeline practice | The vendor-neutral pattern and its tradeoffs | 10 Detection Program Engineering (program structure and strategy) |
| Implementation | What the pattern requires | Platform tracks (how a specific product does it) |

## Labs

N/A

## Datasets

N/A

## References

### Rule Formats and Metadata

- [SigmaHQ Rule Conventions](https://github.com/SigmaHQ/sigma-specification/blob/main/sigmahq/sigmahq-rule-convention.md), SigmaHQ, n.d. Retrieved 2026-11-02.
- [Sigma: Main Sigma Rule Repository](https://github.com/SigmaHQ/sigma), SigmaHQ, n.d. Retrieved 2026-11-02.
- [Alerting and Detection Strategy Framework](https://blog.palantir.com/alerting-and-detection-strategy-framework-52dc33722df2), Palantir, 2017. Retrieved 2026-11-02.

### Pipelines and Deployment

- [Core Component: Managing Detection Rules in a VCS](https://dac-reference.readthedocs.io/en/latest/core_component_managing_detection_rules_in_a_vcs.html), Detection as Code Reference, Elastic, n.d. Retrieved 2026-11-02.
- [Now in beta: New Detection as Code capabilities](https://www.elastic.co/security-labs/dac-beta-release), Mika Ayenson and Eric Forte, Elastic Security Labs, 2024. Retrieved 2026-11-02.
- [CI/CD Detection Engineering: Splunk's Security Content, Part 1](https://www.splunk.com/en_us/blog/security/ci-cd-detection-engineering-splunk-security-content-part-1.html), Splunk, 2020. Retrieved 2026-11-02.

## AI Assistance

None
