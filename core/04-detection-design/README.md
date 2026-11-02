# Detection Design

## Overview

Detection Design covers turning a requirement into a detection approach before writing logic. Learners will be introduced to researching the behavior, forming a testable hypothesis, choosing a detection strategy, mapping to ATT&CK and analyzing coverage, anticipating how the detection will fail, and designing what the resulting alert will display to an analyst.

## Learning Objectives

By the end of this module, learners should be able to:

- Research a behavior to determine how it works and what evidence it leaves.
- Write and test a falsifiable detection hypothesis.
- Select a detection approach, and justify the decision.
- Map detections to ATT&CK and analyze coverage while identifying limitations.
- Express detection logic in pseudocode.
- Anticipate false positives and failure conditions before building.
- Design an alert that gives a responder context.

## Prerequisites

- Module 01: Detection Engineering Foundations
- Module 02: Telemetry & Data
- Module 03: Detection Requirements

## Lessons

### 1. Researching the Behavior

**Learning Objectives**

- Research a behavior to determine how it works and what evidence it leaves.
- Identify variations that reach the same outcome.
- Determine the evidence a behavior leaves in a specific environment.

**Key Topics**

- Capability abstraction
- Procedures and variations
- Research sources
- How a behavior looks in your environment

**Out of scope**

- Turning research into requirements (Module 03)
- Adversary emulation for validation (Module 06)

### 2. Detection Hypotheses

**Learning Objectives**

- Write a falsifiable detection hypothesis.
- Compare hypothesis-driven and indicator-driven detection.
- Test a hypothesis against data before building.
- Scale design depth to a detection's severity.

**Key Topics**

- Falsifiable detection hypothesis
- Hypothesis structure
- Hypothesis-driven vs. indicator-driven detection
- Testing before building
- Multiple hypotheses per behavior
- How much design a detection needs

**Out of scope**

- Sources of detection ideas (Module 03)
- Validation testing (Module 06)

### 3. Choosing a Detection Approach

**Learning Objectives**

- Select an approach (e.g., single event, threshold, sequence, correlation, anomaly) for a hypothesis.
- Evaluate evasion methods.
- Design precise and broad detections that complement each other.
- Determine the context a detection needs.

**Key Topics**

- Detection approaches and when each fits
- Thresholds and time windows
- Evasion considerations
- Detection spectrum and detection in depth
- Base rates as a design input
- Enrichment and baselines a detection depends on

**Out of scope**

- Writing each detection type (Module 05)
- Building enrichment and baselines (Module 02)
- Evasion testing (Module 06)

### 4. ATT&CK Mapping & Coverage Analysis

**Learning Objectives**

- Map a detection to ATT&CK at the right level.
- Analyze coverage across a set of detections, and state limits.
- Explain why a mapping does not show that a technique is detected.

**Key Topics**

- Mapping granularity
- ATT&CK Detection Strategies and Analytics
- Coverage tools
- Coverage quality vs. breadth
- Heatmap pitfalls
- Feeding gaps back to requirements

**Out of scope**

- Prioritizing requirements (Module 03)
- Validating coverage (Module 06)
- Program coverage reporting (Module 10)

### 5. Pseudocode

**Learning Objectives**

- Write detection logic as pseudocode independent of a platform.
- Express each logic pattern in pseudocode.
- Identify over specified and under specified pseudocode.

**Key Topics**

- What the detection does vs. how a platform does it
- Pseudocode structure
- Search, filter, aggregate, threshold
- Logic patterns and time windows
- Reviewable pseudocode
- Common mistakes

**Out of scope**

- Production queries (Module 05)
- Query performance (Module 05)

### 6. Pre-Mortem

**Learning Objectives**

- Identify the legitimate activity that will match a detection, and what separates it from malicious activity.
- Design narrowly scoped exclusions.
- Identify common failures, and whether they are silent or noisy.
- Decide when a detection should not be built as designed.

**Key Topics**

- The cost of false positives and analyst trust
- Sources of false positives
- Pre-analysis questions
- Anticipating false positives without assigning a rate
- Normal is not safe (exclusion blind spots)
- Failure conditions (dependencies, assumptions, and evasions)
- Silent vs. noisy failure
- When not to build

**Out of scope**

- Measuring false positives in production (Modules 08 & 09)
- Tuning (Module 08)
- Evasion testing (Module 06)

### 7. Alert & Response Design

**Learning Objectives**

- Identify what an analyst needs to begin triage.
- Design an alert's title, severity, confidence, description, context, and response guidance.
- Choose between direct alerting and risk-based alerting.

**Key Topics**

- Alert consumers
- Alert anatomy
- Severity vs. confidence
- Risk-based alerting
- Context fields
- Response guidance and pivot queries

**Out of scope**

- Implementing alerts (Module 05)
- Routing, suppression, and deduplication (Module 08)
- Playbooks and automation (Module 08)

### 8. Documenting & Reviewing a Design

**Learning Objectives**

- Document a design using a framework such as ADS.
- Review a design against a checklist.
- Explain why someone other than the author approves a design.

**Key Topics**

- The ADS framework
- Design review vs. code review
- Review process and checklist
- Independent approval and exit criteria
- When a design is sent back

**Out of scope**

- Code review (Modules 05 & 07)
- Repositories, metadata, and catalogs (Module 07)

## Boundaries

| Topic | This module | Adjacent module(s) |
| --- | --- | --- |
| ATT&CK coverage | Mapping and coverage analysis | 03 Detection Requirements (using coverage gaps to prioritize) |
| Alert and response design | What the alert must contain, and why | 05 Detection Development (implementation); 08 Deployment, Tuning & Operations (triage, routing, and suppression in practice) |
| Enrichment | Deciding what context the detection needs | 02 Telemetry & Data (sources and pipelines) |
| Detection types | Choosing an approach | 05 Detection Development (writing each type) |
| Threat research | Researching the behavior to detect | 03 Detection Requirements (intake, and turning research into requirements) |
| Where design ends | A reviewed design with pseudocode | 05 Detection Development (production logic) |
| False positives | Anticipating sources and designing exclusions | 06 Testing & Validation (measurement); 08 Deployment, Tuning & Operations (tuning); 09 Detection Health & Lifecycle (ongoing health) |
| Robustness | Applying the models to a design | 01 Detection Engineering Foundations (concepts); 06 Testing & Validation (evasion testing) |
| Documentation | The design document | 07 Detection-as-Code (repositories, metadata, catalogs) |

## Labs

N/A

## Datasets

N/A

## References

### Behavior Research and Detection Strategy

- [MITRE ATT&CK, v20.0](https://attack.mitre.org/), The MITRE Corporation, 2026. Retrieved 2026-11-02.
- [ATT&CK Detection Strategies](https://attack.mitre.org/detectionstrategies/), The MITRE Corporation, n.d. Retrieved 2026-11-02.
- [ATT&CK Analytics](https://attack.mitre.org/analytics/), The MITRE Corporation, n.d. Retrieved 2026-11-02.
- [Finding Cyber Threats with ATT&CK-Based Analytics](https://www.mitre.org/news-insights/publication/finding-cyber-threats-attck-based-analytics), Blake E. Strom et al., The MITRE Corporation, 2017.
- [Capability Abstraction](https://specterops.io/blog/2020/02/06/capability-abstraction/), Jared Atkinson, SpecterOps, 2020. Retrieved 2026-11-02.
- [Detection Spectrum](https://specterops.io/blog/2020/02/21/detection-spectrum/), Jared Atkinson, SpecterOps, 2020. Retrieved 2026-11-02.

### Hypotheses, Logic, and Design Documentation

- [Alerting and Detection Strategies Framework](https://github.com/palantir/alerting-detection-strategy-framework), Palantir Incident Response Team, 2017. Retrieved 2026-11-02.
- [Sigma Rules Specification, Version 2.1.0](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html), SigmaHQ, 2025. Retrieved 2026-11-02.
- [The Base-Rate Fallacy and the Difficulty of Intrusion Detection](https://dl.acm.org/doi/10.1145/357830.357849), Stefan Axelsson, *ACM Transactions on Information and System Security*, 2000. DOI: 10.1145/357830.357849.
- [NIST SP 800-94: Guide to Intrusion Detection and Prevention Systems](https://csrc.nist.gov/pubs/sp/800/94/final), Karen Scarfone and Peter Mell, National Institute of Standards and Technology, 2007. DOI: 10.6028/NIST.SP.800-94.

### ATT&CK Mapping, Coverage, and Robustness

- [Summiting the Pyramid, Version 4.0.0](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/), MITRE Center for Threat-Informed Defense, 2026. Retrieved 2026-11-02.
- [ATT&CK Navigator](https://github.com/mitre-attack/attack-navigator), The MITRE Corporation, n.d. Retrieved 2026-11-02.
- [DeTT&CT](https://github.com/rabobank-cdc/DeTTECT), Rabobank Cyber Defence Centre, n.d. Retrieved 2026-11-02.
- [How Does Endpoint Detection Use the MITRE ATT&CK Framework?](https://www.usenix.org/conference/usenixsecurity24/presentation/virkud), Apurva Virkud et al., 33rd USENIX Security Symposium, 2024.

### Failure Analysis and Alert Design

- [99% False Positives: A Qualitative Study of SOC Analysts' Perspectives on Security Alarms](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi), Bushra A. Alahmadi, Louise Axon, and Ivan Martinovic, 31st USENIX Security Symposium, 2022.
- [True Attacks, Attack Attempts, or Benign Triggers? An Empirical Measurement of Network Alerts in a Security Operations Center](https://www.usenix.org/conference/usenixsecurity24/presentation/yang-limin), Limin Yang et al., 33rd USENIX Security Symposium, 2024.
- ['Give Me Structure': Synthesis and Evaluation of a (Network) Threat Analysis Process Supporting Tier 1 Investigations in a Security Operation Center](https://www.usenix.org/conference/soups2023/presentation/kersten), Leon Kersten et al., Nineteenth Symposium on Usable Privacy and Security, 2023.
- [Modeling Alerts in OCSF](https://github.com/ocsf/ocsf-docs/blob/main/articles/modeling-alerts.md), Open Cybersecurity Schema Framework Project, n.d. Retrieved 2026-11-02.

## AI Assistance

Research
