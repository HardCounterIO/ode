# Tracks

Tracks extend the [Core](../core/) curriculum into specific areas.

| Directory | Contains |
|---|---|
| [`domains/`](domains/) | Environments and data domains, such as Windows, Linux, cloud, identity, and network |
| [`platforms/`](platforms/) | Specific products and platforms |
| [`advanced/`](advanced/) | Advanced and specialized topics |

**Status:** no tracks yet. Tracks assume the relevant Core material and should link to it rather than repeat it.

## Layout

Each track is a directory in its category, named in lowercase kebab-case (for example `tracks/domains/windows/`). Inside, tracks use the same module structure as Core: numbered module directories with a `README.md`, `module-metadata.yml`, and lessons. See [`core/README.md`](../core/README.md#layout) and [`templates/`](../templates/).

## Expectations

- Follow the [Style Guide](../docs/STYLE-GUIDE.md).
- Platform tracks may go as deep as needed on a product. Marketing material and unsupported vendor claims are not appropriate ([CONTRIBUTING.md](../CONTRIBUTING.md#technical-expectations)).
- Authors and reviewers disclose affiliations with any product covered ([MAINTAINERS.md](../MAINTAINERS.md#affiliation-disclosure)).
- Vendor-specific material should be reviewed by at least one reviewer independent of that vendor where practical ([Review Process](../docs/REVIEW-PROCESS.md#3-roles)).

To propose a track or a module within one, open a [New Module Proposal](https://github.com/ode-os/detection-engineering/issues/new/choose).
