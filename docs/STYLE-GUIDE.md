# Style Guide

This guide defines how ODE content is written so that lessons from different authors read as one curriculum and reviewers have a standard to review against. It applies to Core, tracks, labs, and datasets unless a section says otherwise.

Major changes to this guide (new conventions, changes to the example language, changes to terminology) go through an issue first, as described in [CONTRIBUTING.md](../CONTRIBUTING.md#large-changes).

## 1. Voice and Writing

- Write like a practitioner explaining something to a capable colleague: direct, specific, and concrete.
- Prefer a real operational detail to a generality. "Most environments log this" is weaker than naming the log source and the conditions under which it exists.
- Explain *why* before *how*. A learner who understands why a detection works can adapt it. A learner who only has the query cannot.
- State tradeoffs where legitimate approaches differ. Do not present one approach as the only approach when practitioners disagree.
- Avoid marketing language ("next-gen," "AI-powered," "industry-leading") and filler words that hide difficulty ("simply," "just," "obviously," "trivially").
- Define acronyms on first use in each lesson.
- Use American English, the Oxford comma, and hyphenate compound modifiers (vendor-neutral, practitioner-maintained, high-fidelity).
- Use inclusive terminology: allowlist/denylist, primary/secondary, not whitelist/blacklist or master/slave.
- Write for a global audience: avoid idioms, and spell out dates as `YYYY-MM-DD`.

## 2. Claims and References

- Every non-obvious technical or factual claim must be verifiable. If you cannot point to a source, your own testing, or a clear explanation of the reasoning, remove it or mark it as opinion.
- Prefer primary sources: vendor documentation, specifications, RFCs, original research, and your own reproducible tests. Use secondary sources (blogs, talks) when they are the best available source, and say what they are.
- Every reference is real and checked. Never include a reference you have not opened.
- Detection logic, queries, and code are run against data before submission, and the lesson says what they were tested against.
- Reference format, in each lesson's `## References` section:
  - Title, author or organization, year, and a link.
  - For web pages, add the retrieval date: `Retrieved 2026-10-17`.
  - For papers, include a DOI when one exists.
  - For pages likely to disappear, add an archive link.
- Use short quotations only when exact wording matters, always attributed. Otherwise paraphrase. Do not paste in long passages from other works.
- When a claim depends on a version (a product release, a Windows version, an ATT&CK release), name the version.

### MITRE ATT&CK

- Pin the version: `T1059.001 (ATT&CK vNN)`, where `vNN` is the current release when you write the lesson.
- Use ATT&CK for mapping and shared vocabulary, not as a measure of quality. Do not imply that covering a technique ID means a technique is detected.

## 3. Terminology

These are working definitions for use across ODE. They are proposed, and the Core terminology lesson should settle them. If you disagree with one, open a Discussion or issue rather than redefining it locally.

| Term | Meaning in ODE |
|---|---|
| Telemetry | Raw observations produced by systems, such as logs, traces, and sensor output. |
| Event | A single record within telemetry. |
| Detection | The combination of logic, context, and response expectations that identifies behavior of interest. |
| Detection logic / rule | The codified condition itself: a query, a Sigma rule, a correlation. |
| Alert | The output of a detection that is routed for human or automated triage. |
| True positive | The detection fired and the behavior it targets occurred. |
| Benign true positive | The detection fired correctly on authorized or expected activity. |
| False positive | The detection fired and the targeted behavior did not occur. |
| False negative | The behavior occurred and the detection did not fire. |
| Coverage | What a detection set can observe and detect, expressed with its limits. It is not a count of rules. |

Use "benign true positive" and "false positive" for different things. They have different fixes.

## 4. Vendor Neutrality

- **Core** explains concepts. A product may be named as an illustrative example, never as the only option and never as a recommendation.
- **Platform tracks** may go as deep as needed on a specific product. Marketing material and unsupported vendor claims are not appropriate in any area ([CONTRIBUTING.md](../CONTRIBUTING.md#technical-expectations)).
- Use official product names and capitalization.
- Disclose any affiliation with a product you describe (see the PR template and [MAINTAINERS.md](../MAINTAINERS.md#affiliation-disclosure)).
- Vendor screenshots and UI captures need written permission from the vendor. Prefer your own diagrams.

## 5. Example Languages

### SPL in Core

Core examples use **Splunk SPL** as the reference query language, with Sigma for portable rule logic where useful. SPL is chosen for its readability and familiarity, not because Core teaches Splunk. To keep Core vendor-neutral:

- Explain the logic in plain language first. The SPL expresses it. It is not the lesson.
- Use common commands (`search`, `where`, `eval`, `stats`, `rex`, `sort`, `table`). Avoid Splunk-specific features, such as `tstats`, data models, CIM field normalization, macros, saved-search behavior, and lookups defined in Splunk configuration, in Core. Put those in the Splunk platform track.
- When Core uses SPL, say so once at the top of the module, and note that the technique applies in other query languages.
- Where a lesson is about portability, show the Sigma rule and the SPL together.

Other platform tracks use their native language (KQL, ES|QL, CrowdStrike Query Language, and so on) and may reference the Core logic.

### Conventions

- Use native field names from the log source (for example Sysmon's `Image`, `CommandLine`, `ParentImage`), and name the source. Do not rely on a normalization schema unless the lesson is about that schema.
- Index, sourcetype, and host names are illustrative. Say so.
- One pipe per line, leading pipe, lowercase commands.
- Comment non-obvious steps with SPL's triple-backtick comment syntax.
- Tag fences `spl` for SPL, `yaml` for Sigma, and the appropriate language elsewhere.

```spl
index=endpoint EventCode=1
| where match(CommandLine, "(?i)-enc(odedcommand)?\s")
| stats count by host, User, ParentImage, Image
```

### Sigma

- Include `title`, `id`, `status`, `description`, `references`, `logsource`, `detection`, `falsepositives`, and `level`.
- Use real Sigma field names and logsource taxonomy, not invented ones.

## 6. Example Data and Safety

Examples must not leak real data or be mistaken for it.

- **Domains**: `example.com`, `example.org`, `example.net`, and the reserved TLDs `.example`, `.test`, `.invalid`. Never real domains you do not own.
- **IPv4**: documentation ranges only for external addresses: `192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`. Private ranges (RFC 1918) are fine for internal hosts.
- **IPv6**: `2001:db8::/32`.
- **MAC addresses**: the documentation range `00-00-5E-00-53-00` through `00-00-5E-00-53-FF`.
- **Hosts, users, and organizations**: invented. Do not use real employee names, customer names, or real company names.
- **Credentials**: never real, including revoked or expired ones.
- **Indicators**: no live indicators of compromise. If an indicator is pedagogically necessary, cite its public source and do not include anything that could be harmful if copied.
- **Attack simulation**: describe it at the level needed to build and validate detections. No weaponized payloads, and no live malware, consistent with [SECURITY.md](../SECURITY.md#content-safety-rules). Cite and link public test frameworks rather than reproducing them.

## 7. Structure and Formatting

- Modules and lessons follow the templates in [`templates/`](../templates/). A module's `README.md` is its landing page.
- File names: `NN-kebab-case.md`, e.g. `01-detection-requirements.md`.
- Each lesson states learning objectives that use measurable verbs (write, evaluate, distinguish, justify), not "understand" or "know."
- Title Case for H1 and H2, sentence case below that. One H1 per file.
- One paragraph per line. Do not hard-wrap prose, so diffs stay readable in review.
- Use relative links for internal files. Link text describes the destination ("the review process"), not "click here."
- Fenced code blocks always declare a language.
- Diagrams: provide the source (Mermaid, or the editable file plus an exported SVG), alt text describing the point of the diagram, and keep images in `assets/`.
- Tables are for comparison, not for prose.
- Aim for lessons that can be read in one sitting. If a lesson keeps growing, split it.

## 8. AI-Assisted Writing

AI use is governed by [CONTRIBUTING.md](../CONTRIBUTING.md#ai-assisted-contributions). Style consequences:

- You are responsible for every sentence, query, and reference. Check each one.
- Generic, shallow, or confidently wrong prose fails review whatever produced it.
- Fabricated references and untested detection logic are the most common failures. Check both.

## 9. Checklist for Authors

Before opening a pull request:

- [ ] Learning objectives are measurable.
- [ ] Every claim is verified, and every reference exists and is checked.
- [ ] Detection logic, queries, and code were run against data.
- [ ] Example data follows section 6.
- [ ] Core content is vendor-neutral, or SPL is used per section 5.
- [ ] Versions (ATT&CK, products, OS releases) are named.
- [ ] Metadata is filled in per the [review process](REVIEW-PROCESS.md).
- [ ] Commits are signed off, and affiliations are disclosed.
