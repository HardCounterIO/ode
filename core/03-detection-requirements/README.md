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
