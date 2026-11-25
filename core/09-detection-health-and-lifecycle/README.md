# Detection Health & Lifecycle

## Overview

A detection that worked on the day it was deployed can stop working without raising an error. Its log source can go quiet, a field it depends on can change format or meaning, an untested edit can break its logic, or the threat it targets can stop being relevant. In each case the detection keeps running and shows no alerts, which looks the same as a quiet period. This module teaches how to keep deployed detections healthy over time: who owns their health, the states a detection moves through, how to monitor the data detections depend on and the detections themselves, how to keep validating them, how to troubleshoot a detection that has gone quiet, how to review detections that may have become stale, and how to update, park, or retire them.

Each lesson opens with the failures it addresses. Where lessons include queries, they use Splunk SPL as the Core reference query language; the techniques apply in other query languages.

## Learning Objectives

By the end of this module, learners should be able to:

- Distinguish a quiet detection from a blind one, and a silent failure from a stale detection.
- Justify a detection's lifecycle transitions, from first release to retirement, with health, validation, and review evidence.
- Design source-level and field-level data health checks for a set of detections.
- Evaluate the health of a single detection from its execution, output, and validation signals.
- Diagnose why a detection has stopped alerting.
- Evaluate whether a working detection has become stale, using a defined review cadence and review criteria.

## Prerequisites

- 01 Detection Engineering Foundations: Core vocabulary and the detection lifecycle at overview level.
- 02 Telemetry & Data: log sources, collection, parsing and normalization, and data quality concepts.
- 06 Testing & Validation: test design and adversary emulation methods, which lesson 5 applies over time.

## Lessons

### 1. Detection health and ownership

**Learning objectives**

- Distinguish a quiet detection from a blind one, given its recent results and the state of its data sources.
- Distinguish a silent failure from a stale detection.
- Identify the dependencies a detection relies on between the log source and the alert, and the failure each can introduce without raising an error.
- Assign an owner to each type of health signal (source outage, rule execution error, failed validation, stale-detection review) for a described organization.

**Key topics**

- Detection health as an ongoing responsibility once a detection is deployed
- Quiet versus blind: why zero results is not evidence of health, and why platform status can show green over dead data feeds
- The three health questions: does the detection still receive its data, does it still work, and is it still relevant
- The dependency chain: log source, collection, parsing and normalization, storage, rule logic, scheduled execution, alert routing
- Terms: silent failure (the detection stopped working without raising an error) and stale (the detection still runs but no longer targets a relevant threat or technology), and why each needs a different response
- Ownership of health signals: the detection owner, the log pipeline or platform owner, and the SOC; recording ownership in data collection agreements and SLAs; why ownership models differ between organizations
- Opening example: data feeds that stopped for months while the connection status showed Active

**Out of scope**

- Detection lifecycle overview (01 Detection Engineering Foundations)
- Data quality concepts (02 Telemetry & Data)
- Diagnosing whether a quiet detection is blind (Lesson 6)

### 2. The detection lifecycle in depth

**Learning objectives**

- Describe the states a detection moves through from first release to retirement.
- Justify moving a detection from one state to another using test, health, and review evidence.

**Key topics**

- Why detections need explicit states: what a state tells analysts and engineers about how far to trust a detection
- Published state models, such as the Sigma rule status values (experimental, test, stable, deprecated, unsupported) and the maturity levels and separate enabled flag described in Elastic's Detection Engineering Behavior Maturity Model
- A trial phase before production, and what evidence ends it
- States after release: parked (data source gone, may return), deprecated, retired
- Transitions and their evidence: validation results, time in production, health signals, review outcomes

**Out of scope**

- Lifecycle phases at overview level (01 Detection Engineering Foundations)
- Staged rollout and shadow mode (08 Deployment, Tuning & Operations)
- Versioning and change history for detections (07 Detection-as-Code)
- Deciding whether to fix, park, or retire a detection (Lesson 8)

### 3. Data health: sources and fields

**Learning objectives**

- Classify data failures by their effect on a detection.
- Identify which data failures volume-based source monitoring can and cannot detect.
- Calculate a silence threshold for a log source from its historical arrival gaps.
- Justify source-level or field-level data checks for a detection, based on what each catches and what each costs.

**Key topics**

- Opening: data failures that leave a detection running but blind: a source that stops, partial delivery, a field that disappears, changes format, or changes meaning, a replaced source, a field that arrives empty
- Source and pipeline monitoring: silence, dips, spikes, new or unknown sources, ingest delay
- Per-source baselines and silence thresholds, and filtering trivial drift so data health alerts stay actionable
- Checking arrival per dataset instead of trusting a connector's status
- Replacing a log source when rules are written in Sigma: the logsource abstraction and the conversion pipeline mappings that must be updated
- What source monitoring cannot see: schema, format, and meaning changes at normal volume
- Field-level checks: mapping each detection to the sources and fields it depends on, extracting fields from rule definitions, and checking that those fields are still populated
- Enrichment sources as dependencies: lookups, asset and identity lists, and threat intelligence feeds that go stale, empty, or stop updating while the detection keeps running
- Example: Windows event 4688 records the command line only when a separate policy setting is enabled, so the source looks healthy while command-line detections are blind
- Choosing source-level or field-level checks: the cost of maintaining the dependency map, and criteria such as detection importance, rarely firing detections, and fields that depend on configuration

**Out of scope**

- What good telemetry looks like, parsing, normalization, and schemas (02 Telemetry & Data)
- Building or fixing collection pipelines (02 Telemetry & Data)
- Choosing enrichment sources and judging their quality (02 Telemetry & Data)

### 4. Detection rule health

**Learning objectives**

- Identify rule-side failures that stop a detection from working while its data stays healthy.
- Interpret a detection's health signals to decide whether it needs attention.
- Explain why firing rate alone cannot show the health of a detection that rarely fires.

**Key topics**

- Opening: rule-side failures: untested edits, execution errors, scheduled runs that are skipped or disabled, exclusions that accumulate and are rarely revisited, until they hide the behavior the detection targets
- Execution health: runs that are skipped, start late, time out, fail, or are disabled after repeated failures, and the execution status and health logs that show them (some must be turned on first)
- Output signals: firing rate against its baseline, time since the last alert, sudden drops and spikes
- The low-base-rate problem: a healthy detection that rarely fires and a blind one both show zero alerts
- Combining signals for one detection: data health (Lesson 3), execution, and output

**Out of scope**

- Anticipating failures and designing exclusions before a detection is built (04 Detection Design)
- Tuning noisy detections and analyst feedback loops (08 Deployment, Tuning & Operations)

### 5. Continuous validation

**Learning objectives**

- Select validation checks for a detection based on where each check enters the pipeline and which failures it can detect.
- Justify a validation schedule for a detection that combines periodic and change-triggered runs.
- Identify the owner and lifecycle action for a failed validation result.

**Key topics**

- Opening: a detection that should fire once a year, where no monitoring signal can show whether it still works
- A passing test covers a moment; monitoring covers the time between tests
- Where a check enters the pipeline and what it can see: replayed test events, events sent through an ingestion path, emulation on a real host
- Limits of emulation: sources that cannot be emulated, test hosts configured differently from production, procedures that differ from the one a detection targets
- Cadence: periodic runs, with practitioner suggestions rather than standards, plus runs triggered by changes such as agent updates, parser changes, source replacement, and rule edits
- Automating emulation with public frameworks
- Keeping validation activity from being worked as real incidents: labeling test runs, deconflicting with the SOC, routing matched test alerts away from responders, and reconciling afterwards, without blanket suppression that could hide a real attacker
- Adding validation results to a detection's health signals (Lesson 4)
- Acting on results: who is told, and how a failure changes the detection's state (Lesson 2)

**Out of scope**

- Test design, test data, and writing test cases (06 Testing & Validation)
- Adversary emulation methods and tooling in depth (06 Testing & Validation)
- Running tests in CI before deployment (07 Detection-as-Code)

### 6. Silent failures and troubleshooting

**Learning objectives**

- Diagnose why a detection has stopped alerting by checking data, execution, logic, and validation evidence in order.
- Explain why backtesting a detection on historical data cannot reveal changes in the current data.
- Identify who to escalate to for each failure layer.

**Key topics**

- Opening: a detection with no alerts for three months, and the evidence needed to tell whether it is quiet or blind (Lesson 1)
- A layered troubleshooting order: data arrives at normal volume, is parsed correctly, has its fields populated with unchanged meaning, the rule runs, and its logic still matches
- Evidence for each layer: source and field checks, execution logs, manual runs, replaying modified events into a test index, backtests over periods when the detection fired before
- What backtests show and what they cannot: historical data was parsed by the pipeline as it was then
- Outcomes: fix, park, escalate to the data owner, or send to review (Lesson 7)

**Out of scope**

- Anticipating silent and noisy failure modes at design time (04 Detection Design)
- Writing or rewriting detection logic (05 Detection Development)
- Fixing collection or parsing pipelines (02 Telemetry & Data)
- Triage of individual alerts (08 Deployment, Tuning & Operations)
- Detections that work but are no longer relevant (Lesson 7)

### 7. Stale detections and review cadence

**Learning objectives**

- Identify signs that a working detection has become stale.
- Justify a review cadence for a set of detections based on how often their sources and threats change.
- Evaluate a detection against review criteria: still relevant, still working, and documentation still accurate.

**Key topics**

- Opening: detections that still run correctly but target something that no longer matters
- Stale versus silent failure: different causes with different responses
- Causes of staleness: the targeted technology or platform is retired, the threat is no longer relevant to the organization, a vulnerability is patched (and whether attempts still matter), the technique has evolved past the detection's logic
- What a review checks: relevance against current threat intelligence and the environment, function from health and validation evidence, documentation and metadata
- Cadence: scheduled reviews plus reviews triggered by change, and how maturity models measure review coverage
- Review outcomes: keep, update, change state, retire

**Out of scope**

- The retirement process (Lesson 8)

### 8. Updating, parking, and retiring detections

**Learning objectives**

- Choose between fixing, parking, and retiring a detection based on its health and review findings.
- Assess coverage overlap before retiring a detection.
- Identify the information a retirement record must preserve.

**Key topics**

- Opening: retirement done badly: silent deletion that loses coverage, and detections nobody retires
- Options: fix and revalidate, park (data source gone, may return), deprecate, retire
- Reasons to retire: the technology or threat is gone, the data source is permanently gone, a better detection supersedes it
- Checking overlap and naming a replacement before retiring
- Staged deprecation: marking a detection first, removing it later, and keeping it for analysis of historical data
- Recording the decision: reason, replacement, date, and history
- Parked detections: marked inactive with the reason recorded
- Updating a detection: when a change is significant enough to send it back to a testing state until it is revalidated, and when it is not (Lesson 2)

**Out of scope**

- Writing or rewriting detection logic for a fix (05 Detection Development)
- Designing the tests used to revalidate an updated detection (06 Testing & Validation)
- Version control and removing rules through the deployment pipeline (07 Detection-as-Code)
- Deciding whether a detection is stale (Lesson 7)

## Boundaries

| Topic | This module | Adjacent module(s) |
| --- | --- | --- |
| Detection lifecycle | States, transitions, and end of life in depth | 01 Detection Engineering Foundations (phases at overview level) |
| Detection health terms | Defines and applies silent failure and stale | 01 Detection Engineering Foundations (Core vocabulary) |
| Log source health | Ongoing monitoring of sources, pipelines, enrichment sources, and the fields detections depend on | 02 Telemetry & Data (data quality and enrichment concepts) |
| Failure modes and exclusions | How failures and accumulated exclusions show up in production | 04 Detection Design (anticipating failures and designing exclusions before build) |
| Continuous validation | Running validation over time and acting on results | 06 Testing & Validation (test design, test data, emulation methods) |
| Rule changes | Noticing that a deployed detection broke, and deciding to fix, park, or retire it | 05 Detection Development (writing logic), 06 Testing & Validation (pre-deployment testing), 07 Detection-as-Code (versioning, change history, CI and pipelines) |
| Staged release | States a detection passes through | 08 Deployment, Tuning & Operations (staged rollout and shadow mode) |
| Tuning | Firing rate as a health signal | 08 Deployment, Tuning & Operations (production tuning and analyst feedback) |
| Metrics | Health signals for a single detection | 08 Deployment, Tuning & Operations (per-detection operations), 10 Detection Program Engineering (program metrics and reporting) |
| Ownership | Who owns and receives each health signal | 10 Detection Program Engineering (team structure and roles) |
| Threat relevance | Reviewing whether existing detections are still relevant | 03 Detection Requirements (threat-informed requirements for new detections) |
| Maturity models | Used as references for health practices | 10 Detection Program Engineering |

## Labs

N/A

## Datasets

N/A

## References

### Detection Health and Silent Failure

- [Becoming a Detection and Response Engineer, Part 1: Red Light, Green Light](https://enleak.dev/writing/red-light-green-light), ENLEAK, 2026. Retrieved 2026-10-25.
- [Detection Validation and Decay](https://socprime.com/blog/detection-validation-and-decay/), Brandi Moore, SOC Prime, 2026. Retrieved 2026-10-25.
- [Schrödinger's Detection: Finding the "Zombie" Rules in Your SIEM](https://pretalx.com/fwd-cloudsec-2026/talk/7LUWPZ/), Gowthamaraj Rajendran, fwd:cloudsec, 2026 (talk abstract). Retrieved 2026-10-29.
- [Alerting and Detection Strategies Framework](https://github.com/palantir/alerting-detection-strategy-framework), Palantir Incident Response Team, 2017. Retrieved 2026-10-29.

### Log Source Health

- [Log Health Monitoring](https://lopes.id/log/log-health-monitoring/), lopes.id, 2026. Retrieved 2026-10-25.
- [Logsources](https://sigmahq.io/docs/basics/log-sources.html), SigmaHQ. Retrieved 2026-10-25.
- [Command line process auditing](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/component-updates/command-line-process-auditing), Microsoft Learn, 2025. Retrieved 2026-10-29.

### Detection Rule Health

- [Monitor the health and audit the integrity of your Microsoft Sentinel analytics rules](https://learn.microsoft.com/en-us/azure/sentinel/monitor-analytics-rule-integrity), Microsoft Learn, 2026. Platform-specific example; the same signal exists in other SIEMs. Retrieved 2026-10-29.
- [Investigate skipped scheduled searches](https://help.splunk.com/en/splunk-cloud-platform/administer/admin-manual/10.6/monitor-your-splunk-cloud-platform-deployment/use-the-search-dashboards/investigate-skipped-scheduled-searches), Splunk Cloud Platform 10.6 documentation, Splunk, 2026. Platform-specific example; the same signal exists in other SIEMs. Retrieved 2026-10-29.
- [Fill rule execution gaps](https://www.elastic.co/docs/solutions/security/detect-and-alert/fill-rule-gaps), Elastic Security documentation, Elastic. Platform-specific example; the same signal exists in other SIEMs. Retrieved 2026-10-29.
- [The Exclusion Ratchet: False-Positive Suppression Accumulates and Persists in Detection Rule Repositories](https://arxiv.org/abs/2608.31062), Sudaroli Dhananjeyan and Kumaran U, arXiv preprint (not peer reviewed), 2026. DOI: 10.48550/arXiv.2608.31062. Retrieved 2026-10-29.
- [Handle false positives in Microsoft Sentinel](https://learn.microsoft.com/en-us/azure/sentinel/false-positives), Microsoft Learn, 2026. Platform-specific example of managing exclusions. Retrieved 2026-10-29.

### Lifecycle and Retirement

- [Detection Development Lifecycle](https://medium.com/snowflake/detection-development-lifecycle-af166fffb3bc), Haider Dost, Tammy Truong, and Michele Freschi, Snowflake, 2022. Also a secondary source for ownership in Lesson 1 (detection reviews and validation results). Retrieved 2026-10-29.
- [Rules](https://sigmahq.io/docs/basics/rules.html), SigmaHQ (the rule `status` field). Retrieved 2026-10-25.
- [\[Deprecations\] AWS Elasticache Security Group Rules](https://github.com/elastic/detection-rules/pull/5334), Elastic, detection-rules pull request #5334, 2025. Retrieved 2026-10-25.

### Validation

- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team), Red Canary. Retrieved 2026-10-25.
- [Invoke-AtomicRedTeam](https://github.com/redcanaryco/invoke-atomicredteam), Red Canary. Retrieved 2026-10-25.
- [Caldera](https://github.com/apache/caldera), originally developed by MITRE. Retrieved 2026-10-25.
- [Build an automated detection testing framework with GitLab CI/CD and Duo](https://about.gitlab.com/blog/automated-detection-testing-framework/), Evan Baltman, GitLab, 2026. Retrieved 2026-10-29.

### Maturity Models

- [Detection Engineering Maturity Matrix](https://detectionengineering.io), Kyle Bailey, 2021, updated 2022. Retrieved 2026-10-25.
- [Elastic releases the Detection Engineering Behavior Maturity Model](https://www.elastic.co/security-labs/elastic-releases-debmm), Mika Ayenson, Terrance DeJesus, and Samir Bousseaden, Elastic Security Labs, 2024. Retrieved 2026-10-25.

## AI Assistance

An AI assistant (Claude) was used during research and drafting. The lesson split, lesson order, and boundary decisions were made by the authors in discussion with the assistant. The assistant drafted the wording of the module and lesson learning objectives, key topics, out-of-scope lists, the Boundaries table, and the reference list. The authors reviewed and edited all of this content and opened every reference.
