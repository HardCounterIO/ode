# Risk & Exposure Context

## Overview

Lesson 3 showed how a detection threat model turns threats into requirements. That answers what an adversary might do. This lesson answers a different question: where in this environment would that activity matter most, and where is detection the only control between the adversary and the outcome?

The same technique does not carry the same risk everywhere. Credential dumping on a lobby kiosk is a different problem than credential dumping on a domain controller. An exploit for a vulnerability patched last month is a different problem than an exploit for a system that cannot be patched until next year. Asset criticality, exposure, and vulnerability state are the context that turns a generic requirement into one scoped to the environment it protects.

This lesson covers where that context comes from, how to use vulnerability intelligence such as the Cybersecurity and Infrastructure Security Agency (CISA) Known Exploited Vulnerabilities (KEV) catalog, the Exploit Prediction Scoring System (EPSS), and the Common Vulnerability Scoring System (CVSS) without being misled by them, and when detection should act as a compensating control for risk the organization cannot remediate in the near term. Combining these inputs into a final priority is covered in Lesson 6.

## Core Content

### Asset Criticality

Asset criticality is how much harm the organization suffers if an asset is compromised. It depends on what the asset does for the business, what data it holds, and what access it grants to other systems. Risk assessment frameworks such as National Institute of Standards and Technology (NIST) Special Publication (SP) 800-30 Rev. 1 treat impact as one of the core factors of risk alongside likelihood. Asset criticality helps a detection engineer estimate the potential impact of compromising a specific system.

Crown-jewel systems are the ones whose compromise is the outcome the organization most fears: payment processing, customer data stores, or the systems that run a core business process. The systems that grant access to the crown jewels matter almost as much. Domain controllers, identity providers, backup infrastructure, and software build pipelines are often more valuable to an attacker than the data itself, because control of them gives access to many other systems.

The same technique warrants different priority on different assets. A new service created on an ordinary workstation may be routine software deployment. The same event on a backup server or a domain controller is more unusual, because those systems usually change less often, and it is far more damaging if missed. A requirement that treats both the same either hides the important alerts among routine ones or under-protects the systems that matter most.

Criticality shapes a requirement in three ways. It narrows **scope**, because a requirement can target a defined set of high-criticality assets rather than the whole environment. It raises **priority**, which Lesson 6 covers in depth. And it changes the **tolerance for alert volume**, because a missed compromise costs more on a critical asset, so each alert is worth more investigation time. On a domain controller, a detection that fires a few extra times a week may be acceptable, while the same rate on each of thousands of workstations would overwhelm triage. Higher criticality does not excuse a noisy detection, because alerts that analysts learn to ignore are not investigated.

Criticality data is often wrong. Asset tiers in a configuration management database (CMDB) are frequently set once and never revisited, and asset owners may not know what depends on their systems. Treat recorded criticality as a starting point, and confirm it with the asset owner before building a requirement around it.

Sometimes the problem is not a wrong rating but a missing asset. An owner leaves the organization, and no one else knows the system exists. A system is assumed to be decommissioned but is still running. A server built quickly during an outage or incident never goes through normal provisioning and never reaches the inventory. These assets are often unpatched and unmonitored, which makes them a likely place for an attacker to gain a foothold without being noticed. A detection requirement scoped to "all critical assets" silently excludes them, so treat inventory gaps as a known limit of any asset-scoped requirement.

### Attack Surface and Exposure

Exposure is how reachable an asset is to an attacker. Criticality describes what is lost if an asset is compromised. Exposure describes who is in a position to attempt that compromise, and by what paths. The attack surface is the set of all the ways in: network services, accounts, and connections to other organizations.

Internet-facing systems are the most exposed. Remote access gateways such as virtual private network (VPN) concentrators, web applications, email, and file transfer services can be reached by any attacker without first compromising something else. Their logs also show a steady stream of scanning and failed attempts from sources that have nothing to do with a targeted attack. A requirement for an internet-facing asset is therefore usually more useful when it targets evidence that an attempt succeeded, such as the service starting an unexpected process or a new account appearing on the system, than when it targets individual attempts. Attempts are still worth a requirement when they show knowledge of the organization, such as sign-in failures against many valid account names from one source.

Internal does not mean unexposed. Exposure depends on where the attacker is, and after one workstation is compromised, the attacker is inside. On a network with little internal segmentation, a database server that every workstation can reach is exposed to whoever controls any workstation. Internal exposure is described by what can reach the asset: which network segments, which accounts, and which management tools.

Exposure is not always direct. An asset with no internet connectivity can still be reached through a system that has it. If an internet-facing application server holds a service account with access to an internal database, an attacker who compromises the application server has a path to the database. When assessing exposure, follow the systems, accounts, and trust relationships that lead to the asset, not only whether the asset itself can be reached from the internet.

Identity is part of the attack surface. An asset behind a strong network boundary is still exposed if an account that can administer it is weakly protected. The accounts that add the most exposure are those without multi-factor authentication (MFA), service accounts with long-lived credentials that are shared across systems, privileged accounts that sign in to many systems, and accounts that are no longer used but remain enabled. Identity exposure lets a requirement be scoped to specific accounts rather than specific hosts, for example, a service account signing in interactively or from a host it has never used.

Third-party access extends the attack surface to organizations whose security the detection team cannot observe or control. Vendors with remote support access, managed service providers, and partners with application programming interface (API) credentials can all reach internal systems, and a compromise on their side becomes access to the organization. When vendor access is granted for a defined purpose, with specific accounts, source addresses, systems, and maintenance windows, the expected pattern is known in advance. That makes it a good subject for a requirement, because activity outside the pattern can be defined precisely. Where vendor access is broad or undocumented, record that as a gap, because no requirement can separate expected vendor activity from misuse without a defined pattern to compare against.

Exposure shapes a requirement's scope and priority as criticality does, and it also changes what the requirement looks for, because the likely path to an asset determines which behaviors are worth detecting on it. The two are assessed together: an exposed path to a critical asset is the case that most needs a requirement. Combining them into a final priority is covered in Lesson 6.

Exposure also changes more often than criticality. A firewall rule change, a new cloud resource, or a newly published service can expose an asset that was internal the day before. Exposure can also close when a service is disabled, or vendor access is revoked. Later sections cover where current exposure data comes from and when an exposure-driven requirement should be retired.

### Vulnerability State as a Detection Input

Vulnerability state is what is known about the weaknesses on an asset: which known vulnerabilities are present, whether they are being exploited elsewhere, and whether a fix has been applied. For detection, it helps answer a question the threat model cannot: of everything an attacker might try, which known weaknesses are present here? A vulnerability that is present, exposed, and not yet remediated marks a place where a requirement may be the only control until the fix arrives.

Three public sources describe vulnerability state from different angles. Each answers one question well, and as published, none of them knows anything about the environment.

#### CISA KEV: Confirmed Exploitation

The KEV catalog lists vulnerabilities that CISA has determined were exploited in the wild. CISA adds an entry when a vulnerability has a Common Vulnerabilities and Exposures (CVE) identifier, there is reliable evidence of active exploitation, and there is a clear remediation action. Each entry also records whether the vulnerability is known to be used in ransomware campaigns. An entry marked unknown has not been confirmed either way.

For a detection requirement, a KEV entry is the strongest evidence of exploitation among the three sources, because it replaces a prediction with a fact: attackers have already used this vulnerability. That is evidence about the vulnerability, not about the risk to a particular asset. If a KEV vulnerability is present on an asset that cannot be remediated quickly, that asset is a strong candidate for a requirement.

KEV has three limits. It is not complete, and it trails the attackers: an entry appears only after exploitation is confirmed, so absence from the catalog does not mean exploitation is not happening. It is a yes-or-no record, so it says nothing about how widely a vulnerability is exploited or against whom. And it covers only vulnerabilities with a CVE identifier and a remediation action, which leaves out misconfigurations and most flaws in internally developed software.

#### EPSS: Likelihood of Exploitation

EPSS is a model maintained by the Forum of Incident Response and Security Teams (FIRST) that estimates, for each published CVE, the probability that exploitation activity will be observed in the next 30 days. Scores range from 0 to 1 and are recalculated daily. Each score is published with a percentile that ranks it against all other scored CVEs. The two numbers are easy to confuse: because most CVEs score near zero, a high percentile can correspond to a low probability.

EPSS is useful for the large set of vulnerabilities that are present in the environment but not in KEV. A vulnerability on an exposed asset whose EPSS score is high or rising is a candidate for a requirement before any exploitation is confirmed.

EPSS has limits that matter for detection. The probability describes exploitation activity observed by the organizations that contribute data to the model, anywhere on the internet. It does not describe activity against a particular organization, and the model has no knowledge of an asset's exposure or criticality. The activity it predicts includes unsuccessful and blocked attempts, not only successful compromise. A low score is an estimate, not an assurance. And because scores change daily, a decision made on last month's score may no longer hold. FIRST describes EPSS as an estimate of exploitation likelihood, not a complete risk score.

#### CVSS: Severity, Not Risk

CVSS, also maintained by FIRST, describes the technical characteristics of a vulnerability and produces a severity score from 0 to 10. Version 4.0 names scores by the metric groups used: CVSS-B is a Base score alone, and CVSS-BTE adds Threat and Environmental metrics, which account for exploit maturity and for the organization's own environment. The scores published by vendors and vulnerability databases are usually Base scores only. The same caution applies to version 3.1 scores, which remain common in scanner output.

A Base score describes how bad exploitation could be in general, with no reference to whether anyone is exploiting the vulnerability or where the vulnerable system sits. The CVSS documentation is explicit that a Base score measures severity and should not be used alone to assess risk. A requirement driven by Base score alone can lead a team to spend effort on critical-rated vulnerabilities on isolated systems while overlooking medium-rated ones on exposed systems that attackers are using.

The part of CVSS that helps a detection engineer most is the vector string, not the number. The vector records how the vulnerability is reached and what exploitation gives the attacker, and that indicates what behavior a requirement should target. A vulnerability with a network attack vector and no privileges required can be attempted by anyone who can reach the service, so the requirement concerns what the service does after exploitation. A vulnerability with a local attack vector cannot be reached over the network. It is exploited by someone who can already run code on the system, or by a user who is persuaded to open a malicious file. In the first case, the requirement concerns a change in privilege by an account already present on the host. In the second, it concerns what the application does after it opens the file.

#### Using The Three Together

| Source | Question it answers | What it does not show |
| --- | --- | --- |
| CISA KEV | Has this vulnerability been exploited? | How widely, or whether unconfirmed exploitation is occurring |
| EPSS | How likely is exploitation activity in the next 30 days? | Whether attempts will succeed, or whether they will reach this organization |
| CVSS Base Score | How severe is exploitation, and how is it carried out? | Whether anyone is exploiting the vulnerability|

None of the three shows whether the vulnerability is present in the environment, whether the affected asset is exposed, or how much that asset matters. The organization's own data provides those answers. A vulnerability most clearly warrants a requirement when it is present on an asset that is exposed or critical, and it cannot be remediated before an attacker is likely to use it.

Vulnerability state also has an end date. Once a vulnerability is remediated, a requirement written because of it may no longer be needed, which the requirement expiry section covers. How to weigh these inputs against threat relevance, feasibility, and effort is covered in Lesson 6.

### Detection as a Compensating Control

A compensating control is an alternative measure used to reduce a risk when the preferred control cannot be applied. For a vulnerable system, the preferred control is remediation: patching, upgrading, or reconfiguring it. When remediation is not possible in the near term, a detection requirement can reduce the risk while the vulnerability remains.

Detection is not prevention. A detection requirement does not stop exploitation. It can shorten the time an attacker operates unnoticed after exploitation, but only if the alert is investigated and acted on before the harm is done. A compensating requirement therefore has to state who responds to an alert and what they can do, such as isolating the system or disabling an account. That response has to be possible for the specific system: a database that supports a business-critical application may not be something anyone is permitted to isolate, and alerts that arrive when no one is monitoring may not be seen until it is too late. A requirement that produces alerts no one can act on compensates for nothing.

#### Why Remediation is Deferred

Many organizations depend on legacy systems that have reached end-of-life (EOL) or end-of-support (EOS). Depending on the vendor's lifecycle policy, these systems may no longer receive security updates or technical support. Point-of-sale systems, legacy reporting applications, and the databases behind them are common examples, because they support processes the business cannot stop and they were built for a platform that has since been retired. Remediation is deferred for reasons that are usually legitimate:

- **Cost:** Replacing the system may mean new hardware, new licensing, or rebuilding an application.
- **Operational downtime:** The upgrade may take a business-critical process offline, or it may have to wait for a period when the process can be interrupted.
- **Vendor dependencies:** The application may be supported only on the old platform, or the vendor may no longer exist.

Remediation plans also stall partway through. A project to replace a legacy system can run for months and then stop when it reaches a dependency no one had documented, such as another application that relies on the old system. A compensating requirement covers the time until remediation happens, however long that turns out to be.

#### Treating Detection as an Interim Control

A compensating requirement exists because of a specific gap, and it should say so. When remediation remains the goal, the requirement is tied to the remediation plan: it names the vulnerability or EOL condition it compensates for, the plan to remove that condition, the owner of that plan, and the expected remediation date. Without that link, the requirement outlives its purpose, and the organization may also stop treating the remediation as urgent because a control is in place.

Detection is not always the right compensating control. If the time from exploitation to harm is shorter than the time it takes to respond, detection cannot prevent the harm, and a preventive measure such as isolating the system from networks that do not need to reach it is the better investment. Lesson 6 covers the choice between detection, prevention, and accepting the risk.

#### Scoping a Compensating Requirement

A compensating requirement is narrower than a general requirement for the same technique because it is written for one known gap. Its scope comes from what was established in the previous sections:

- **Assets:** the specific systems that carry the vulnerability or EOL condition, not every system of that type.
- **Exposure:** the paths by which an attacker can reach those systems, which determine where exploitation would start and what it would look like.
- **Behavior:** the activity associated with exploitation or with later compromise of the system. CVSS metrics describe the conditions exploitation requires, and vendor advisories and technical reporting on the vulnerability describe how it has been exploited.
- **Response:** who acts on an alert, and what action is available for this system.
- **Timeline:** the remediation milestone the requirement depends on, and the date it should next be reviewed.

EOL does not always mean unmonitored. Endpoint agents often continue to support an operating system for some time after its vendor ends support, so a legacy system may still produce the telemetry a requirement needs. That support is not permanent, and it should be confirmed for each system rather than assumed. When no agent supports the system, a requirement may have to depend on telemetry from the network around it, from the systems it communicates with, or from the accounts that sign in to it. Whether the available telemetry can support a requirement is covered in Lesson 5.

### Missing or Failed Preventive Controls

Preventive controls reduce how much reaches detection. Multi-factor authentication (MFA) blocks sign-ins that use a stolen password alone, application control blocks unapproved programs, and network segmentation blocks connections that have no business reason. Where a preventive control is in place and working, a requirement for the behavior it blocks matters less. Where it is missing or has failed, detection carries more of the weight.

#### Missing Controls

Some controls were never applied to part of the environment. Common examples are systems that do not enforce MFA, networks with little internal segmentation, and hosts where application control was never deployed. Exceptions belong in the same category, because an exception is a control that is missing for a defined set of accounts or systems: accounts exempted from MFA, folders excluded from endpoint protection scanning, and firewall rules opened for a single project and never closed. Each gap marks a behavior that prevention would have stopped and nothing now stops. A record of gaps and exceptions is a direct source of scope for requirements, because it names the accounts and systems where detection is the only control.

#### Failed Controls

Some controls were applied and then stopped working. An endpoint agent is disabled or stops reporting, a firewall rule is removed or broadened, MFA enforcement is turned off for troubleshooting, or application control is switched from blocking to audit-only mode. Some failures are caused by attackers, because disabling defenses is a common step before the rest of an attack; MITRE ATT&CK describes it as Impair Defenses (T1562, ATT&CK v20.1). Others are caused by administrators, by a failed update, or by a change that was meant to be temporary.

A failed control creates two kinds of requirements. The first targets the failure itself: a protection being disabled, a security policy being weakened, or an agent going silent. Because legitimate administrative changes produce the same events, this kind of requirement needs a way to recognize authorized changes, such as a change ticket or an approved administrative account, so that expected changes are identified as benign true positives rather than investigated from scratch. The second covers the period while the control is down: requirements for the behaviors the control normally blocks become more important until it is restored.

#### When The Failure is Silent

A control that stops working often produces no event at all. An agent that has been uninstalled stops sending data, and a log source that has stopped forwarding produces nothing. To a detection, missing data looks the same as no activity. Requirements that depend on a control or a log source should state how its absence would be noticed, for example by alerting when a host has not reported within an expected interval. Monitoring the health of telemetry sources in general is covered in Module 02 and Module 09.

### Requirement Expiry

Requirements driven by exposure or vulnerability state depend on a condition that is expected to change. A compensating requirement exists because a system cannot be patched, and that system will eventually be patched or replaced. A requirement scoped to an exposed service exists because the service is reachable, and that exposure can be closed. When the condition changes, the requirement may no longer be needed, or may need a different scope. A requirement that outlives its condition still costs effort to maintain and investigate, and it can give a false impression of what the detection program is protecting.

#### Conditions That Trigger Review

An exposure-driven requirement should be reviewed when any of the conditions it depends on change:

- The vulnerability is remediated.
- The asset is decommissioned.
- The exposure is closed; for example, a service is no longer published to the internet or vendor access is revoked.
- A preventive control that was missing or had failed is applied or restored.
- The remediation date passes without the remediation being completed.

The requirement itself should record these conditions, along with a review date and an owner, as described in the section on scoping a compensating requirement. A review date is a fallback for changes no one reports. Reaching it triggers a review, not automatic retirement: a requirement whose condition still exists should not lose its coverage because a date passed.

#### Verify Before Retiring

A change record that says a condition is resolved is not proof that it is. A patch can be marked as deployed and fail to install on some systems. A system can be marked as decommissioned and still be running, as described in the asset criticality section. Exposure changes need the same check: removing one firewall rule does not close the exposure if another path still reaches the asset, and revoking one vendor account does not end vendor access if the vendor has a second one. Before retiring a requirement, confirm the change with evidence: a rescan showing the vulnerability is gone, a version check on the affected software, a review of the current network and access configuration, or confirmation that the decommissioned system no longer appears on the network.

#### Outcomes of a Review

A review has three possible outcomes:

- **Retire:** the condition is resolved and verified, and the behavior the requirement targets is no longer more likely or more harmful on these assets than elsewhere.
- **Re-scope:** the original condition is resolved, but the behavior still matters. The requirement is kept with an updated justification, scope, and priority that no longer depend on the resolved condition. Lesson 6 covers re-prioritization.
- **Extend:** the condition still exists. The requirement is kept with a renewed justification and a new review date, and if remediation has slipped, the delay is raised with the remediation owner rather than absorbed silently.

Retiring a requirement does not mean disabling the detections that implement it. A detection written for one requirement may also satisfy others, or have value of its own, and its future is a separate decision. Retiring and maintaining detections is covered in Module 09.

When a requirement is retired, keep a record of why it existed and why it was retired. If the condition returns, such as a vulnerability reintroduced by restoring an old system image, the record lets the team restore the requirement quickly instead of starting over.

### Sources of Exposure Context

The previous sections depend on data the detection team usually does not own: which assets exist, how critical they are, what can reach them, and which vulnerabilities they carry. That data comes from tools and teams across the organization. Each source sees part of the environment, and each has gaps a detection engineer should know before building a requirement on it.

#### Vulnerability Scanning

Vulnerability scanners report which known vulnerabilities are present on which assets. They are the main source of vulnerability state. Their output is only as complete as their coverage and configuration: a scanner reports nothing about assets it does not scan, and an unauthenticated scan sees only what a system exposes over the network, so it can miss vulnerabilities that are visible only in installed software or local configuration. Authenticated scans see more, but only when their credentials are valid and have enough permissions. Findings also age between scans. A requirement built on scanner data should note which assets the scanner covers and when the data was collected.

#### Asset Inventory and CMDB

An asset inventory or CMDB records what assets exist, who owns them, and what they do, and it is often where criticality ratings are stored. It is the source for scoping a requirement to a defined set of assets and for finding the person to confirm details with. As the asset criticality section describes, it is often incomplete or out of date: assets are missing, owners have left, and ratings were set once and not revisited.

#### Attack Surface Management

External attack surface management (ASM) tools discover and monitor what the organization exposes to the internet, from the outside, the way an attacker would see it. They often find assets that internal records miss, such as forgotten web servers, test environments, or services published by another team. They are a direct source for the internet-facing exposure described earlier. Discovery alone does not show whether an exposure is authorized or vulnerable, and these tools do not show internal exposure or the paths available once an attacker is inside.

#### Cloud Posture Management

Cloud security posture management (CSPM) tools read configuration from cloud provider platforms and report exposure there, such as storage that is publicly accessible and resources with network rules open to the internet. Identities with more permissions than they use are reported by cloud infrastructure entitlement management (CIEM) tools, a related category that many platforms combine with CSPM. Cloud resources can be created and changed in minutes, so findings should be checked against current configuration, and coverage extends only to the cloud accounts the tool is connected to.

#### Other Sources

Exposure context also comes from records that are not security tools. Firewall and network configuration shows which segments can reach an asset. Identity and directory data shows which accounts can administer it, which lack MFA, and which are no longer used. Vendor access records and contracts show which third parties can reach the environment and on what terms. Each is owned by a different team, and each can be the most authoritative record of its own area when that team keeps it current.

#### Reconciling Sources

No single source is complete, and the places where sources disagree are often the most useful findings. An asset that appears in scanner results but not in the inventory may be unmanaged or missing an owner. A service that an ASM tool finds on the internet but the inventory records as internal may be an exposure no one approved. A system in the inventory that no scanner has reported on recently may be offline, or may be unscanned. When building a requirement, check its scope against more than one source, and treat a disagreement between sources as a finding to resolve, not an error to ignore.

## Examples

The organizations, systems, and scores in these examples are invented for illustration.

### Example 1: A Compensating Requirement for a Legacy Reporting Server

An organization runs a reporting application on a server whose operating system reached end of support two years ago. The application vendor supports only that operating system, and the project to replace the application has stalled on an undocumented dependency: the finance team's month-end process reads directly from the application's database.

A vulnerability is published in the reporting application. The evidence looks like this:

- **CISA KEV:** listed, with exploitation confirmed in the wild.
- **EPSS:** a high probability, in the top few percent of scored vulnerabilities.
- **CVSS Base:** high, with a network attack vector, no privileges required, and no user interaction.

The detection engineer then gathers what the public sources cannot show:

- **Presence:** The vulnerability scanner confirms the vulnerable version on the server, `rpt-app-01`.
- **Criticality:** The CMDB rates the server as medium. The finance team confirms that month-end close depends on it and that the database holds customer billing records, so the engineer records it as high and asks for the CMDB rating to be corrected.
- **Exposure:** The server is not internet-facing, but the network has little internal segmentation, so every workstation can reach the application's web port. The application also holds a service account with read access to the billing database.
- **Remediation:** The patch requires a newer operating system, so it cannot be applied until the replacement project is complete. The project owner estimates six months.
- **Telemetry:** The endpoint agent still supports the server's operating system and reports process and network activity.

Each part of the risk is present: confirmed exploitation, a reachable path, a critical asset, and no near-term remediation. The engineer writes a compensating requirement:

- **Behavior:** the reporting application's process starting a command interpreter or other unexpected child process, or making outbound connections to destinations it does not normally contact.
- **Data:** process creation and network connection events from the endpoint agent on `rpt-app-01`.
- **Conditions:** any child process of the application not on the list of processes the application is known to start, and any outbound connection outside its documented destinations.
- **Context:** compensating control for the reporting application vulnerability on an EOS server. Remediation owner: the application replacement project lead. Expected remediation date: six months from today. Review date: monthly, and when the replacement project reports a milestone.
- **Success criteria:** an alert reaches the security operations team within minutes, at any hour. The responder is authorized to block the server's network access, because finance has agreed that a few hours of reporting downtime is acceptable compared with a compromise of billing data.

The engineer also records a recommendation for a preventive measure: restricting access to the application's web port to the finance team's subnet. This narrows the exposure while the requirement is in place, and Lesson 6 covers weighing it against the requirement.

At the six-month review, the replacement project has not finished: the finance team's month-end process still has to be moved to the new application. The condition still exists, so the engineer extends the requirement with a renewed justification and a new review date one month out, and raises the delay with the project lead rather than letting the review date move silently.

A month later, the replacement project reports that the old server is decommissioned. Before retiring the requirement, the engineer confirms that `rpt-app-01` no longer responds on the network and no longer reports to the endpoint agent, and that the scanner no longer finds the vulnerable version anywhere. The original condition is resolved and verified. The engineer retires the requirement and keeps its record. The detection itself, an unexpected child process from a web-facing application, remains useful elsewhere, so whether to keep it for other applications is passed to the detection owners as a separate decision.

### Example 2: A Critical Score That Does Not Warrant a Requirement

The same organization's scanner reports a vulnerability with a CVSS Base score of 9.8 on a server in a test lab.

- **CISA KEV:** not listed.
- **EPSS:** a low probability.
- **Exposure:** The lab network is isolated from the corporate network and the internet, and only two engineers have accounts on the server.
- **Criticality:** low. The server holds no production data, and it is rebuilt from a standard image every week.
- **Remediation:** A patch is available and scheduled for the next rebuild, in five days.

The high Base score describes how severe exploitation could be, but nothing else in the evidence supports a requirement. No path reaches the server except through two known accounts, the server holds nothing of value, and the exposure ends in five days. The engineer does not write a compensating requirement and record the reasoning, so that if the lab is later connected to the corporate network, the decision can be revisited.

## Operational Considerations

### Dependence on Other Teams

Almost every input in this lesson is owned by another team: vulnerability data by vulnerability management, asset records by IT operations, network rules by network engineering, identity data by identity administrators, and remediation plans by application owners. A detection team that only reads these sources learns about changes late. The conditions that trigger a review of an exposure-driven requirement, such as a patch deployed, an asset decommissioned, or a firewall rule changed, are usually recorded by someone else first. Where possible, agree with those teams on how the detection team is told about changes that its requirements depend on, such as change management notifications, remediation status updates, or asset lifecycle records, and record who is responsible for sending them, rather than relying on review dates alone.

### Linking to Risk Exceptions

Many organizations already have a process for approving a deferred remediation or an accepted risk, often called a risk exception. A risk exception and a compensating requirement usually concern the same gap but record different things: the exception records the organization's approval to defer remediation, and the requirement records the detection expected while the risk remains. Linking them, so that each refers to the other, keeps the two from drifting apart. The exception's expiry should trigger a review of the requirement, alongside the requirement's own review conditions, and an exception renewed without discussion should prompt the question of whether the requirement was also extended without a new justification.

### Scale

An environment with many legacy systems can produce more compensating requirements than a team can maintain, if each vulnerability on each system gets its own. Where several vulnerabilities share an asset, an exposure path, a response, and the same observable exploitation behavior, one requirement scoped to the shared condition is easier to maintain than one per vulnerability. For example, several vulnerabilities in web applications on EOS servers reachable from the general workstation network may all lead to the application starting unexpected processes. Vulnerabilities that are exploited in different ways need separate requirements even when they share an asset, because grouping them would leave some exploitation behavior uncovered. Track the number of active compensating requirements, their age, and their review dates. A growing count or rising average age can indicate that deferred remediation is accumulating.

### Making Deferred Risk Visible

A compensating requirement manages the risk of deferred remediation. It does not remove that risk, and a requirement that has been documented is not yet a working control until its detection is implemented, tested, and has a team to respond. Even when it works, the organization pays for the delay in detection effort, investigation time, and the risk that remains because detection is not prevention. That cost is easy to lose when the requirement exists only in the detection team's backlog. Reporting compensating requirements alongside the remediation they wait on, for example in the same risk report, keeps the remediation from being treated as solved because a control is in place.

### Common Failure Modes

- **Building on stale data:** scoping a requirement from a scan or inventory export that no longer reflects the environment. Record the date of the data a requirement was built on.
- **Treating a source as complete:** scoping to "all critical assets" from one inventory, which silently excludes assets that inventory does not know about.
- **Letting reviews lapse:** review dates that pass without a review, which turns temporary requirements into permanent ones without anyone deciding to keep them.
- **Retiring on a change record:** retiring a requirement because a ticket says the condition is resolved, without verifying it.
- **Compensating on paper:** a requirement that is documented or implemented but whose alerts no one is available, trained, or authorized to investigate and act on.

## References

- [NIST SP 800-30 Rev. 1: Guide for Conducting Risk Assessments](https://csrc.nist.gov/pubs/sp/800/30/r1/final), Joint Task Force Transformation Initiative, National Institute of Standards and Technology, 2012. DOI: 10.6028/NIST.SP.800-30r1.
- [Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), Cybersecurity and Infrastructure Security Agency, n.d. Retrieved 2026-11-24.
- [Reducing the Significant Risk of Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities), Cybersecurity and Infrastructure Security Agency, n.d. Retrieved 2026-11-24.
- [Exploit Prediction Scoring System](https://www.first.org/epss/), Forum of Incident Response and Security Teams, n.d. Retrieved 2026-11-24.
- [Exploit Prediction Scoring System: Frequently Asked Questions](https://www.first.org/epss/faq.html), Forum of Incident Response and Security Teams, n.d. Retrieved 2026-11-24.
- [How EPSS Works](https://www.first.org/epss/how-it-works.html), Forum of Incident Response and Security Teams, n.d. Retrieved 2026-11-24.
- [Common Vulnerability Scoring System, Version 4.0: Specification Document](https://www.first.org/cvss/v4.0/specification-document), Forum of Incident Response and Security Teams, 2023.
- [Common Vulnerability Scoring System, Version 4.0: User Guide](https://www.first.org/cvss/v4.0/user-guide), Forum of Incident Response and Security Teams, 2025.
- [Impair Defenses, Technique T1562](https://attack.mitre.org/techniques/T1562/), MITRE ATT&CK v20.1, The MITRE Corporation, 2026. Retrieved 2026-11-24.
