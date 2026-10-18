# Security Policy

ODE is primarily educational content, but it also includes lab tooling, datasets, and attack-simulation material. This policy covers how to report problems in those areas.

## Scope

Please report privately:

1. **Vulnerabilities** in ODE-maintained lab tooling, scripts, or automation.
2. **Sensitive data committed by mistake**: credentials, API keys, personal data, customer data, or proprietary material in any lab, dataset, or document.
3. **Unsafe content**: for example, a lab that exposes the learner's machine or network, or a sample that is live malware.

Not in scope for private reporting (use the **Technical Correction** issue template instead, marking it security-sensitive):
- Inaccurate or misleading detection guidance, including guidance that would create a blind spot if followed.

## Reporting

Use GitHub's private vulnerability reporting:
[Report a vulnerability](https://github.com/ode-os/detection-engineering/security/advisories/new)

If that is unavailable, email <tj@tallisjordan.com> with:
- a description of the issue and where it is (file, lab, dataset)
- steps to reproduce, if applicable
- your assessment of impact

Do not open a public issue or pull request for these reports.

## What to expect

ODE is volunteer maintained. We aim to:
- acknowledge your report within 5 business days
- give you an initial assessment within 14 days
- remove sensitive data from the repository promptly, and rewrite history where needed
- credit you in the fix or advisory unless you prefer otherwise

There is no bug bounty.

## Supported versions

ODE is pre-1.0. Only the `main` branch is supported.

## Content safety rules

- No live malware or weaponized exploit code is committed to this repository.
- Attack simulation is described at the level needed to build, test, and validate detections.
- Datasets must be synthetic, generated for ODE, or properly licensed and scrubbed of real personal, customer, credential, or proprietary data (see [LICENSE.md](LICENSE.md#datasets)).

## Good-faith research

If you make a good-faith effort to follow this policy, avoid harming others, and report promptly, we will not pursue action against you. This policy does not cover third-party systems.
