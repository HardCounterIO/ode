# Detection Engineering Foundations

## Overview

This module starts learners off with why detection exists and why it became an engineering discipline. Learners are then introduced to treating the practice as a software engineering discipline, where detections are introduced as systems rather than just queries. Detection Engineering is also distinguished from other functions that work alongside it: security operations center (SOC), incident response (IR), cyber threat intelligence (CTI), and threat hunting. With this foundation, learners are then introduced to the shared vocabulary for the Core modules, mental models used to help reason about detections, and closes with the detection lifecycle, mapping each phase to the Core module that covers it in depth.

This module is conceptual. It does not teach how to build, test, or operate a detection engineering program; those are the subjects of Modules 02 through 10.

## Learning Objectives

By the end of this module, learners should be able to:

- Explain why detection is necessary alongside prevention, and how the field moved from signature-based to behavior-based detection.
- Describe a detection as a system of inputs, processing, outputs, and dependencies, and explain why detections must be treated as more than a query alone.
- Define detection engineering, compare it with alternative definitions, and distinguish it from SOC operations, incident response, threat intelligence, and threat hunting by what each produces and consumes.
- Apply the ODE vocabulary consistently.
- Use common detection engineering mental models to explain concepts such as increasing the difficulty for adversaries to evade detection.
- Sequence the phases of the detection lifecycle, and identify the Core module that covers each phase.

## Prerequisites

- Understanding of at least one log source (endpoint, network, or cloud).
- Ability to read and understand raw event logging, YAML, or other structured data.
- Ability to read and understand simple queries in any language (SPL, KQL, ES|QL, SQL).

## Lessons

### 1. Why Detection Exists

**Learning Objectives**

- Explain why detection is necessary.
- Explain differences between signature-based and behavior-based detection.
- Trace development of detection from early to modern systems and methods.

**Key Topics**

- Prevention failures
- Detection prior to computing
- Early security monitoring
- Signature era
- Pyramid of Pain
- Detecting behaviors rather than indicators
- Why detection can be hard, and why detection engineering started

**Out of scope**

- Pyramid of Pain in depth (Lesson 5)
- Methods for measuring detection performance

### 2. Detection as an Engineering Discipline

**Learning Objectives**

- Describe a detection as a system of inputs, processing, outputs, and dependencies.
- Apply the definition of engineering to detection work, and identify the phases teams often skip.

**Key Topics**

- A detection is not just a query: inputs, processing, outputs, and dependencies
- Where detection logic runs: SIEM, EDR, etc.
- Engineering as a systematic, disciplined, quantifiable approach (IEEE / SWEBOK)
- Mapping detection work to software engineering knowledge areas
- Why skipping engineering phases leads to poor detections
- Analyst trust as the outcome of engineering

**Out of scope**

- The detection lifecycle
- Log sources, collection, parsing, and pipelines

### 3. What Detection Engineering Is (and Isn't)

**Learning Objectives**

- Working definition of detection engineering; compare with alternatives.
- Distinguish detection engineering from the SOC, IR, CTI, and threat hunting by what each produces and consumes.
- Explain the guiding principles of detection engineering practice.
- Explain why to practice Detection-as-Code (treating detections as software).

**Key Topics**

- Working definitions of detection engineering and differences
- What detection engineering is not
- Guiding principles
- Interfaces between detection engineering and SOC, IR, CTI, and threat hunting teams
- State of the field

**Out of scope**

- Team structure, staffing, career paths, and program metrics
- SOC triage processes
- Detection-as-Code implementation (e.g., repositories, CI/CD)

### 4. Core Vocabulary

**Learning Objectives**

- Define key vocabulary (e.g., telemetry, event, detection, analytic, alert, incident).
- Classify detection outcomes (e.g., true positive, benign true positives, false positives, etc); explain differences between benign and false positives.
- Define coverage.

**Key Topics**

- ODE glossary
- Outcome categories
- ATT&CK detection strategies, analytics, data components, and log sources
- Contested terms and ODE's choices
- Fidelity defined

**Out of scope**

- Measuring detection quality
- Data schemas and normalization
- Coverage analysis

### 5. Mental Models

**Learning Objectives**

- Use common mental models to explain detection engineering concepts.
- Explain the differences between precise and broad detections and applicability to the scenario.
- Compare signature, behavioral, correlation, and anomaly-based detection approaches.
- Explain why mapping a detection to an ATT&CK technique does not show that a technique is covered.

**Key Topics**

- Pyramid of Pain
- Summiting the Pyramid
- Capability abstraction
- Detection spectrum and detection in depth
- Detection approaches and trade-offs
- Models (e.g., Cyber Kill Chain)

**Out of scope**

- Applying, scoring, or mapping detections
- Testing
- Writing detection logic

### 6. The Detection Lifecycle

**Learning Objectives**

- Sequence the phases of the detection lifecycle from start to finish.
- Relate the software development lifecycle to the detection lifecycle.
- Compare the ODE lifecycle with at least one other published detection lifecycle.
- Identify the Core module that covers each lifecycle phase.

**Key Topics**

- ODE detection lifecycle
- Software lifecycle stages applied to detections
- Published lifecycles for comparison
- Feedback from SOC, IR, and threat hunting
- Why detections decay (high level; e.g., tuning, exclusions, drift)
- How each phase maps to Modules 02 to 10

**Out of scope**

- The depth of any individual phase
- Health monitoring, decay, and retirement in depth (Module 09)

## Boundaries

| Topic | This module | Adjacent module(s) |
| --- | --- | --- |
| Core vocabulary | Defines the terms used across Core and settles the Style Guide's working definitions | All modules use these terms and propose changes by issue or PR |
| Detection lifecycle | Phases, sequence, and feedback loops at overview level | 09 Detection Health & Lifecycle (health, decay, retirement), 08 Deployment, Tuning & Operations |
| Detection-as-Code | Concept and reasoning for use | 07 Detection-as-Code |
| Role of detection engineering | Definition and interfaces with SOC, IR, CTI, and threat hunting | 10 Detection Program Engineering (team design, program, metrics) |
| Telemetry and data | Defines telemetry, event, and log source | 02 Telemetry & Data |
| Requirements and prioritization | Named lifecycle phase | 03 Detection Requirements |
| Mental models | Concepts and shared vocabulary | 04 Detection Design, 06 Testing & Validation |
| Detection accuracy (e.g., false positives) | Outcomes & definitions | 04 Detection Design (consideration), 06 Testing & Validation (measurement), 08 Deployment, Tuning & Operations (tuning) |
| Documentation of detections | Not covered | 04 Detection Design |
| Rule formats and query languages | Not covered | 05 Detection Development, 07 Detection-as-Code, platform tracks outside Core |
| Maturity models | Not covered | 10 Detection Program Engineering |

## Labs

N/A

## Datasets

N/A

## References

### History and Foundations

- [Computer Security Technology Planning Study, Volume II](https://seclab.cs.ucdavis.edu/projects/history/papers/ande72.pdf), James P. Anderson, Electronic Systems Division, Air Force Systems Command, 1972.
- [Computer Security Threat Monitoring and Surveillance](https://seclab.cs.ucdavis.edu/projects/history/papers/ande80.pdf), James P. Anderson, James P. Anderson Company, 1980.
- An Intrusion-Detection Model, Dorothy E. Denning, *IEEE Transactions on Software Engineering*, 1987. DOI: 10.1109/TSE.1987.232894.
- [The Base-Rate Fallacy and the Difficulty of Intrusion Detection](https://dl.acm.org/doi/10.1145/357830.357849), Stefan Axelsson, *ACM Transactions on Information and System Security*, 2000. DOI: 10.1145/357830.357849.
- [Intrusion and Intrusion Detection](https://users.ece.cmu.edu/~adrian/731-sp04/readings/ijis-published.pdf), John McHugh, *International Journal of Information Security*, 2001. DOI: 10.1007/s102070100001.
- [Intrusion Detection: A Brief History and Overview](https://sites.cs.ucsb.edu/~vigna/publications/2002_kemmerer_vigna_IntrusionDetection.pdf), Richard A. Kemmerer and Giovanni Vigna, *IEEE Computer*, 2002.
- [99% False Positives: A Qualitative Study of SOC Analysts' Perspectives on Security Alarms](https://www.usenix.org/conference/usenixsecurity22/presentation/alahmadi), Bushra A. Alahmadi, Louise Axon, and Ivan Martinovic, USENIX Security Symposium, 2022.

### Detection Engineering as a Discipline

- [Alerting and Detection Strategies Framework](https://github.com/palantir/alerting-detection-strategy-framework), Palantir Incident Response Team, 2017.
- [11 Strategies of a World-Class Cybersecurity Operations Center](https://www.mitre.org/sites/default/files/2022-04/11-strategies-of-a-world-class-cybersecurity-operations-center.pdf), Kathryn Knerr and Carson Zimmerman, The MITRE Corporation, 2022.
- [Practical Threat Detection Engineering](https://www.packtpub.com/en-us/product/practical-threat-detection-engineering-9781801076715), Megan Roddie, Jason Deyalsingh, and Gary J. Katz, Packt, 2023.
- [The NIST Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), National Institute of Standards and Technology, 2024.
- [Guide to the Software Engineering Body of Knowledge (SWEBOK Guide), Version 4.0a](https://www.computer.org/education/bodies-of-knowledge/software-engineering), IEEE Computer Society, 2025.
- [SP 800-61 Rev. 3: Incident Response Recommendations and Considerations for Cybersecurity Risk Management](https://csrc.nist.gov/pubs/sp/800/61/r3/final), National Institute of Standards and Technology, 2025.

### Vocabulary and ATT&CK

- [MITRE ATT&CK, v20.0](https://attack.mitre.org/), The MITRE Corporation, 2026.
- [ATT&CK Detection Strategies](https://attack.mitre.org/detectionstrategies/), The MITRE Corporation.
- [ATT&CK Updates: October 2025 (v18)](https://attack.mitre.org/resources/updates/updates-october-2025/), The MITRE Corporation, 2025.

### Mental Models

- [The Pyramid of Pain](https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html), David J. Bianco, 2013 (revised 2014).
- [Capability Abstraction](https://specterops.io/blog/2020/02/06/capability-abstraction/), Jared Atkinson, SpecterOps, 2020.
- [Detection Spectrum](https://posts.specterops.io/detection-spectrum-198a0bfb9302), Jared Atkinson, SpecterOps.
- [Summiting the Pyramid](https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/), MITRE Center for Threat-Informed Defense.
- [How does Endpoint Detection use the MITRE ATT&CK Framework?](https://www.usenix.org/conference/usenixsecurity24/presentation/virkud), Apurva Virkud et al., USENIX Security Symposium, 2024.

### Detection Lifecycle

- [Detection Development Lifecycle](https://medium.com/snowflake/detection-development-lifecycle-af166fffb3bc), Haider Dost, Tammy Truong, and Michele Freschi, Snowflake, 2022.
