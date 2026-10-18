# Core

The Core curriculum contains vendor-neutral knowledge applicable to Detection Engineering regardless of platform or environment.

**Status:** no modules yet. The structure below is a starting proposal from the [roadmap](../ROADMAP.md), and the final structure is to be decided collaboratively. To propose changes, open a [Curriculum Proposal](https://github.com/HardCounterIO/ode/issues/new/choose).

## Proposed Areas

1. Detection Engineering Foundations
2. Detection Requirements
3. Telemetry & Data
4. Detection Design
5. Detection Development
6. Testing & Validation
7. Detection-as-Code
8. Deployment, Tuning & Operations
9. Detection Health & Lifecycle
10. Detection Program Engineering

## Layout

Each module is a directory named `NN-slug`, for example `01-detection-engineering-foundations/`:

```text
core/
  01-detection-engineering-foundations/
    README.md              # module landing page (from templates/module-template.md)
    module-metadata.yml    # from templates/module-metadata.yml
    01-what-is-a-detection.md
    02-...
```

- The `slug` in `module-metadata.yml` must match the directory name without its number prefix. CI checks this.
- Start from the files in [`templates/`](../templates/).

## Writing and Review

- Follow the [Style Guide](../docs/STYLE-GUIDE.md). Core uses SPL as a reference query language, with the constraints described there.
- Core content is vendor-neutral. Products belong in [platform tracks](../tracks/platforms/).
- Content moves through the statuses in the [Review Process](../docs/REVIEW-PROCESS.md). New modules start with an issue ([CONTRIBUTING.md](../CONTRIBUTING.md#large-changes)).
