# Detection Requirements 
## Overview 
Covers deciding what to detect and in what order: where detection ideas come from, how to turn them into actionable requirements, and how to prioritize them against threats and the organization's actual risk and exposure.

## Learning Objectives
By the end of this module, learners should be able to: 
* TBD

## Prerequisites
TBD 

## Lessons
### 4. Risk & Exposure Context

#### Learning Objectives

- Explain how asset criticality, exposure, and vulnerability state change the priority of a detection requirement
- Use vulnerability intelligence (KEV, EPSS, CVSS) as inputs to detection requirements and describe the limits of each
- Identify when detection should act as a compensating control for risk that cannot be remediated in the near term
- Scope a compensating detection requirement to the asset's exposure and its remediation timeline

#### Key Topics

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

#### Out of Scope

- Operating a vulnerability management program (scanning cadence, patching workflows, SLAs)
- Combining risk factors into a final priority (Lesson 6)
- Telemetry required to observe exploitation (Module 02)
- Building exploitation detections (Module 05) 
***
### 6. Prioritization

#### Learning Objectives

- Combine threat, impact, exposure, feasibility, and effort into a defensible priority for a detection requirement
- Evaluate the strengths and failure modes of common prioritization approaches
- Decide when a risk should be addressed through detection, prevention, or explicit acceptance
- Communicate prioritization decisions to stakeholders in terms of risk reduction

#### Key Topics

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

#### Out of Scope

- Detailed treatment of exposure and asset risk inputs (Lesson 4)
- Assessing telemetry availability (Lesson 5)
- Program-level backlog management, capacity planning, and metrics (Module 10)

## Boundaries
TBD

## Labs
None yet

## Datasets
None yet

## References
- MITRE ATT&CK
- CISA Known Exploited Vulnerabilities (KEV) Catalog
- FIRST Exploit Prediction Scoring System (EPSS)
- MITRE Center for Threat-Informed Defense (CTID) publications
