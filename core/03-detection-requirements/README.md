# Detection Requirements

## Overview

Covers deciding what to detect and in what order: where detection ideas come from, how to turn them into actionable requirements, and how to prioritize them against threats and the organization's actual risk and exposure.

## Learning Objectives

By the end of this module, learners should be able to:

- Write a detection requirement that states the behavior, required data, triggering conditions, context, and success criteria.
- Identify where detection ideas come from, and evaluate an idea's relevance to the environment.
- Extract detection requirements from a detection threat model.
- Use asset criticality, exposure, and vulnerability state to shape the priority and scope of a requirement.
- Determine whether a requirement can be met with available telemetry within organizational constraints.
- Prioritize requirements and communicate the decisions in terms of risk reduction.

## Prerequisites

- Module 01: Detection Engineering Foundations
- Module 02: Telemetry & Data

## Lessons

### 1. What A Detection Requirement Is

**Learning Objectives**

- Explain why requirements come before design, and why a blocked requirement is a valid outcome.
- Scope a vague detection request into a defined problem.
- Write a requirement that states the behavior, data, conditions, context, and success criteria.

**Key Topics**

- Starting from the problem, not a query
- Scoping questions (who, which systems, what data, what priority, what response)
- Visibility problems vs. detection problems
- Minimum contents of a requirement
- Verify, don't assume
- Requirements vs. hypotheses and designs

**Out of scope**

- Sources of detection ideas (Lesson 2)
- Feasibility in depth (Lesson 5)
- Hypotheses and design (Module 04)

### 2. Sources of Detection Ideas

**Learning Objectives**

- Identify the sources detection ideas come from.
- Evaluate an idea's relevance to the environment.
- Explain why every request goes through the same intake.

**Key Topics**

- Threat intelligence
- Incidents and post-incident reviews
- Red team, penetration test, and purple team findings
- Threat hunting
- ATT&CK as a source
- Compliance and stakeholder requests
- News driven requests

**Out of scope**

- Researching a behavior (Module 04)
- Running a threat intelligence or threat hunting program
- Prioritizing ideas (Lesson 6)

### 3. Threat-Informed Requirements

**Learning Objectives**

- Build a detection threat model.
- Translate threat scenarios into expected behaviors and required telemetry.
- Use ATT&CK to provide structure and find gaps without using it as a checklist.
- Derive requirements from a threat model.

**Key Topics**

- Why "detect everything" fails
- Threat modeling for detection
- Who attacks, what they want, how they get in, what they do next, and what they leave behind
- Threats to behaviors to telemetry to gaps to requirements
- ATT&CK as a tool
- Living threat models

**Out of scope**

- Asset and exposure context (Lesson 4)
- Coverage analysis of existing detections (Module 04)
- Researching a behavior in depth (Module 04)

### 4. Risk & Exposure Context

**Learning Objectives**

- Explain how asset criticality, exposure, and vulnerability state change the priority of a detection requirement.
- Use vulnerability intelligence (KEV, EPSS, CVSS) as inputs to detection requirements and describe the limits of each.
- Identify when detection should act as a compensating control for risk that cannot be remediated in the near term.
- Scope a compensating detection requirement to the asset's exposure and its remediation timeline.

**Key Topics**

- Asset criticality: business impact, crown-jewel systems, and why the same technique warrants different priority on different assets
- Attack surface and exposure: internet-facing versus internal, identity exposure, and third-party or vendor access
- Vulnerability state as a detection input:
  - CISA KEV: confirmed exploitation in the wild
  - EPSS: likelihood of exploitation
  - CVSS: severity rather than risk, and why it should not drive priority alone
- Detection as a compensating control:
  - End-of-life and end-of-support systems the business depends on, such as point-of-sale systems and legacy reporting applications or databases
  - Why remediation is often deferred: upgrade cost, operational downtime, and vendor dependencies
  - Treating detection as an interim control while remediation remains a long-term goal
- Missing or failed preventive controls: where prevention is absent, detection carries more weight
- Requirement expiry: re-evaluating or retiring exposure-driven requirements when the exposure is remediated or the asset is decommissioned
- Sources of exposure context: vulnerability scanning, asset inventory and CMDB data, attack surface management, and cloud posture management

**Out of scope**

- Operating a vulnerability management program (scanning cadence, patching workflows, SLAs)
- Combining risk factors into a final priority (Lesson 6)
- Telemetry required to observe exploitation (Module 02)
- Building exploitation detections (Module 05)

### 5. Feasibility

**Learning Objectives**

- Map a requirement to the log sources, events, and fields it needs.
- Rate a requirement's feasibility.
- Identify platform, organizational, and compliance constraints.
- Record an unsupported requirement as a telemetry gap.

**Key Topics**

- Environment assessment (Module 02) vs. per-requirement feasibility
- Field level data source mapping
- Whether the requirement needs a baseline
- Platform, organizational, and compliance constraints
- Whether the SOC can act on the result
- Tracking blocked requirements

**Out of scope**

- Assessing log source quality (Module 02)
- Closing telemetry gaps (Module 02)
- Detection design (Module 04)

### 6. Prioritization

**Learning Objectives**

- Combine threat, impact, exposure, feasibility, and effort into a defensible priority for a detection requirement.
- Evaluate the strengths and failure modes of common prioritization approaches.
- Decide when a risk should be addressed through detection, prevention, or explicit acceptance.
- Communicate prioritization decisions to stakeholders in terms of risk reduction.

**Key Topics**

- Prioritization inputs: threat relevance, potential impact, asset exposure, telemetry feasibility, and engineering effort
- Prioritization approaches:
  - Qualitative tiers (high / medium / low)
  - Weighted scoring models
  - Threat-driven ranking (for example, prevalence of techniques in relevant threat activity)
  - Coverage-gap-driven ranking
- Failure modes:
  - Headline-driven priority: high-profile news creating pressure to act on threats with little relevance to the environment
  - Severity over exposure: letting a single input such as CVSS outrank actual exposure and exploitability
  - Remediation-only planning: relying on a long remediation effort that later stalls on an undiscovered dependency, with no interim detection in place
  - False precision in scoring models, and prioritizing what is easy to build over what matters
- Detect, prevent, or accept: when detection is the right investment and when the better answer is a preventive control or documented risk acceptance
- Re-prioritization triggers: new threat intelligence, incidents, environment changes, and remediated exposure
- Explaining priority to stakeholders: tying decisions to risk reduction rather than rule counts, and grounding responses to headline threats in actual exposure

**Out of scope**

- Detailed treatment of exposure and asset risk inputs (Lesson 4)
- Assessing telemetry availability (Lesson 5)
- Program-level backlog management, capacity planning, and metrics (Module 10)

## Boundaries

| Topic | This module | Adjacent module(s) |
| --- | --- | --- |
| ATT&CK coverage | Using coverage gaps to prioritize | 04 Detection Design (mapping and coverage analysis) |
| Telemetry feasibility | Whether a specific requirement can be met | 02 Telemetry & Data (assessing and improving sources) |
| Threat research | Intake and turning research into requirements | 04 Detection Design (researching the behavior to detect) |
| Backlog and intake process | Per-requirement intake and prioritization | 10 Detection Program Engineering (program level) |
| Vulnerability management | Vulnerability state as a detection input | Operating a vulnerability management program is not covered in Core |
| Baselines | Identifying when a requirement needs one | 02 Telemetry & Data (establishing baselines); 04 Detection Design (using them) |
| Hypotheses and design | Not covered | 04 Detection Design |

## Labs

N/A

## Datasets

N/A

## References

### Detection Requirements and Sources

- [Alerting and Detection Strategies Framework](https://github.com/palantir/alerting-detection-strategy-framework), Palantir Incident Response Team, 2017.
- [SP 800-61 Rev. 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final), Alexander Nelson, Sanjay Rekhi, Murugiah Souppaya, and Karen Scarfone, National Institute of Standards and Technology, 2025. DOI: 10.6028/NIST.SP.800-61r3.
- [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), National Institute of Standards and Technology, 2024. DOI: 10.6028/NIST.CSWP.29.

### Threat-Informed Requirements

- [MITRE ATT&CK, v20.0](https://attack.mitre.org/), The MITRE Corporation, 2026. Retrieved 2026-11-01.
- [The Design and Philosophy of MITRE ATT&CK](https://attack.mitre.org/docs/ATTACK_Design_and_Philosophy_March_2020.pdf), Blake E. Strom et al., The MITRE Corporation, 2020.
- [ATT&CK Detection Strategies](https://attack.mitre.org/detectionstrategies/), The MITRE Corporation, n.d. Retrieved 2026-11-01.
- [Top ATT&CK Techniques](https://ctid.mitre.org/projects/top-attack-techniques), MITRE Center for Threat-Informed Defense, 2024. Retrieved 2026-11-01.

### Risk and Exposure Context

- [NIST SP 800-30 Rev. 1: Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Joint Task Force Transformation Initiative, National Institute of Standards and Technology, 2012. DOI: 10.6028/NIST.SP.800-30r1.
- [NIST IR 8286A Rev. 1: Identifying and Estimating Cybersecurity Risk for Enterprise Risk Management](https://csrc.nist.gov/pubs/ir/8286/a/r1/final), Stephen Quinn et al., National Institute of Standards and Technology, 2026.
- [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), Cybersecurity and Infrastructure Security Agency, n.d. Retrieved 2026-11-01.
- [Exploit Prediction Scoring System](https://www.first.org/epss/), Forum of Incident Response and Security Teams, n.d. Retrieved 2026-11-01.
- [Common Vulnerability Scoring System, Version 4.0](https://www.first.org/cvss/v4.0/specification-document), Forum of Incident Response and Security Teams, 2023.
- [Stakeholder-Specific Vulnerability Categorization Guide](https://www.cisa.gov/sites/default/files/publications/cisa-ssvc-guide%20508c.pdf), Cybersecurity and Infrastructure Security Agency, n.d. Retrieved 2026-11-01.

### Feasibility and Prioritization

- [Top ATT&CK Techniques Methodology](https://center-for-threat-informed-defense.github.io/top-attack-techniques/), MITRE Center for Threat-Informed Defense, 2024. Retrieved 2026-11-01.
- [CISA Cross-Sector Cybersecurity Performance Goals](https://www.cisa.gov/cross-sector-cybersecurity-performance-goals), Cybersecurity and Infrastructure Security Agency, n.d. Retrieved 2026-11-01.

## AI Assistance

Research
