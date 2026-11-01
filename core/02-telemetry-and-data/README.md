# Telemetry & Data

## Overview

This module covers the data that detections run on. Learners examine where telemetry comes from, how it is collected and parsed, where data is stored, how to assess whether it is trustworthy and compatible for a given detection. This module also covers how normalization, enrichment, and baselines prepare data for use in detection.

Module 01 established that a detection is a system, and that its inputs are part of that system. This module is about those inputs. Learners should be able to assess whether their environment's data can support detection, explain where data can fail, and describe what it would take to close the gaps.

This module uses native field names for examples rather than a normalized schema.

## Learning Objectives

By the end of this module, learners should be able to:

- Describe the major categories of security telemetry and what each can and cannot show.
- Trace an event from the system that produces it to the platform where detections are run, and identify where it can be lost, delayed, or altered.
- Compare data architecture on cost, retention, latency, resilience, searchability, and processing.
- Assess a log source's fitness to support detection and document visibility gaps.
- Evaluate the trade-offs of normalization approaches and common schemas.
- Explain how enrichment and baselines add context that raw events lack, and how each can fail.

## Prerequisites

- Module 01: Detection Engineering Foundations

## Lessons

### 1. Telemetry & Log Sources

**Learning Objectives**

- Distinguish telemetry, events, sensors, log sources, and ATT&CK Data Components.
- Categorize telemetry (endpoint, network, identity, cloud, application) by the activity each can show.
- Identify common visibility gaps and failures of each category.
- Relate a log source to the ATT&CK Data Components.

**Key Topics**

- Telemetry forms: audit and application logs, traces, metrics, network flows and packets, snapshots, sensor events, etc.
- Source categories and what each answers
- What each telemetry form and source category can and cannot show
- Native event names and field names
- ATT&CK Data Components and Log Sources
- Data dictionaries (e.g., OSSEM)

**Out of scope**

- Configuring logging for specific systems (domain tracks)
- Choosing sources for a specific requirement (03)

### 2. Collection and Parsing

**Learning Objectives**

- Compare common collection and transport methods and their common failures.
- Trace an event from source to search, and identify where it can be lost, delayed, or altered.
- Distinguish event, ingestion, and processing time; explain how clock skew affects detection.
- Explain how parsing, schema drift, and pipeline behavior affect the trustworthiness of detection data.

**Key Topics**

- Collection methods (agents, forwarding, etc.)
- Pipeline stages
- Filtering at the source
- Buffering, retries, duplicates, out of order delivery
- Parsing, field extraction, character encoding, and schema drift
- Event time vs. ingestion time
- Silent data loss and partial failure
- Pipeline as a detection dependency

**Out of scope**

- Building and operating pipelines (platform tracks)
- Pipeline health monitoring (09)

### 3. Where Detection Data Lives

**Learning Objectives**

- Compare indexed, data lake, and other architectures on cost, retention, latency, and normalization effort.
- Distinguish batch from streaming detection.
- Explain how retention and storage limit lookback and investigation.
- Explain how access, integrity, privacy, and minimization requirements affect telemetry storage.

**Key Topics**

- Comparison of data architectures
- Storage and retention
- Batch vs. streaming
- Collection decisions
- Cost, retention, latency, resilience, and searchability
- Sensitive data in telemetry: access, privacy, and minimization

**Out of scope**

- Platform strategy and selection (10)
- Query performance (05)

### 4. Assessing Data Quality & Visibility

**Learning Objectives**

- Build a log source inventory.
- Evaluate a log source for completeness, accuracy, validity, consistency, timeliness, uniqueness, and integrity.
- Determine whether data supports a detection need fully, partially, or not at all.
- Document visibility gaps and how each finding was verified.

**Key Topics**

- Ingested is not the same as usable
- Log source inventory
- Data quality characteristics
- Measuring coverage and field population
- Assessments

**Out of scope**

- Feasibility of a specific requirement (03)
- Prioritizing which gaps to close (03)
- Log source health monitoring (09)

### 5. Normalization & Schemas

**Learning Objectives**

- Compare methods of normalization.
- Evaluate field reliability and planning for missing fields.
- Compare common schemas and what normalization gains and loses.

**Key Topics**

- The normalization problem
- Normalization methods
- Preserving raw values
- Field reliability
- Value normalization
- Field dictionaries
- Common schemas (OCSF, OSSEM, role of platform data models)

**Out of scope**

- Writing detections against a schema (05)
- Platform data models (platform tracks)

### 6. Enrichment

**Learning Objectives**

- Distinguish enrichment from normalization.
- Identify common enrichment sources.
- Compare ingest time, query time, and alert time enrichment.
- Evaluate enrichment data for freshness, provenance, confidence, temporal correctness, and join reliability.

**Key Topics**

- Identity, asset, threat intelligence, and behavioral context
- Ingest time, query time, and alert time enrichment
- Source provenance and confidence
- Stale context and lookup failures
- Enrichment as a detection dependency

**Out of scope**

- Deciding what context a detection needs (04)
- Monitoring enrichment sources (09)

### 7. Baselines

**Learning Objectives**

- Explain what a baseline is, and why it is local to an environment.
- Distinguish volumetric, temporal, and behavioral baselines.
- Establish and validate a baseline for a defined entity and metric.
- Explain why normal is not the same as safe.

**Key Topics**

- Static vs. calculated baselines
- Volumetric, temporal, and behavioral baselines
- Choosing the window, entities, and metrics
- Environmental change and baseline drift
- Baselines that include compromised activity

**Out of scope**

- Using baselines in logic, thresholds, and exclusions (04, 05)
- Machine learning for anomaly detection

## Boundaries

| Topic | This module | Adjacent module(s) |
| --- | --- | --- |
| Telemetry Vocabulary | Applies the Module 01 definitions | 01 Detection Engineering Foundations |
| Enrichment | Sources, stages, and common failures | 04 Detection Design (deciding on context for a detection) |
| Data architecture | Architecture and trade offs | 05 Detection Development (query performance); 10 Detection Program Engineering |
| Visibility gaps | Identifying what is and is not collected | 03 Detection Requirements (feasibility, and prioritizing gaps to close) |
| Log source health | Data quality concepts and assessment | 09 Detection Health & Lifecycle (monitoring) |
| Normalization and schemas | What they are and trade offs | 05 Detection Development (writing queries against sources) |
| Baselines | Establishing what normal looks like | 04 Detection Design (using baselines to choose approaches, thresholds, and exclusions); 05 Detection Development (implementation) |
| Sensitive data | Access, privacy, and minimization | 10 Detection Program Engineering (governance) |
| Source specific logging configuration | Not covered | Domain tracks |
| Platform ingestion and data models | Not covered | Platform tracks |

## Labs

N/A

## Datasets

N/A

## References

### Telemetry and log management

- [Best Practices for Event Logging and Threat Detection](https://www.cyber.gov.au/publication/best-practices-for-event-logging-and-threat-detection), Australian Signals Directorate's Australian Cyber Security Centre and international partners, 2024. Retrieved 2026-10-31.
- [NIST SP 800-92: Guide to Computer Security Log Management](https://csrc.nist.gov/pubs/sp/800/92/final), Karen Kent and Murugiah Souppaya, National Institute of Standards and Technology, 2006. DOI: 10.6028/NIST.SP.800-92.
- [NIST SP 800-92 Rev. 1: Cybersecurity Log Management Planning Guide, Initial Public Draft](https://csrc.nist.gov/pubs/sp/800/92/r1/ipd), Karen Scarfone and Murugiah Souppaya, National Institute of Standards and Technology, 2023. DOI: 10.6028/NIST.SP.800-92r1.ipd.
- [NIST SP 800-53 Rev. 5: Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), Joint Task Force, National Institute of Standards and Technology, 2020, Release 5.2.0 published 2025. DOI: 10.6028/NIST.SP.800-53r5.

### ATT&CK and Visibility

- [MITRE ATT&CK, v20.0](https://attack.mitre.org/), The MITRE Corporation, 2026. Retrieved 2026-10-31.
- [ATT&CK Updates: October 2025, v18](https://attack.mitre.org/resources/updates/updates-october-2025/), The MITRE Corporation, 2025. Retrieved 2026-10-31.
- [OSSEM: Open Source Security Events Metadata](https://github.com/OTRF/OSSEM), Open Threat Research Forge, n.d. Retrieved 2026-10-31.

### Collection, formats, and time

- [OpenTelemetry Logs Data Model](https://opentelemetry.io/docs/specs/otel/logs/data-model/), OpenTelemetry Project, n.d. Retrieved 2026-10-31.
- [RFC 5424: The Syslog Protocol](https://www.rfc-editor.org/rfc/rfc5424), Internet Engineering Task Force, 2009.
- [RFC 5425: Transport Layer Security Transport Mapping for Syslog](https://www.rfc-editor.org/rfc/rfc5425), Internet Engineering Task Force, 2009.

### Data quality and schemas

- [ISO/IEC 25012: Software Engineering — Software Product Quality Requirements and Evaluation — Data Quality Model](https://www.iso.org/standard/35736.html), International Organization for Standardization, 2008.
- [Open Cybersecurity Schema Framework](https://ocsf.io/), OCSF Project, n.d. Retrieved 2026-10-31.

### Enrichment and baselines

- [STIX Version 2.1](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html), OASIS Open, 2021. Retrieved 2026-10-31.
- [NIST SP 800-94: Guide to Intrusion Detection and Prevention Systems](https://csrc.nist.gov/pubs/sp/800/94/final), Karen Scarfone and Peter Mell, National Institute of Standards and Technology, 2007. DOI: 10.6028/NIST.SP.800-94.
