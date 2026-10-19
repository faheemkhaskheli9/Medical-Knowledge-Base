# Contributing

## Content rules
- Every clinical fact must have a source from [`sources.md`](docs/sources.md).
- Every file starts with front matter:

```yaml
---
title: <name>
last_reviewed: YYYY-MM-DD
reviewed_by: <name, credential>
sources:
  - <citation>
region: global | US | UK | EU | PK | ...
---
```

- Write doses as `<amount> <unit> <route> <frequency>` (e.g. `500 mg PO every 12 hours`). Use leading zeros (`0.5 mg`), no trailing zeros (`5 mg`, not `5.0 mg`).
- Mark region-specific content clearly.
- Re-review each file at least every 12 months, or when a guideline or label changes.

## Review
- Clinical content should be reviewed by a licensed professional (physician, pharmacist) before merge.
- Record changes to recommendations in the commit message with the reason and source.

## Adding a drug
Copy [`medicines/_template.md`](docs/medicines/_template.md) into `docs/medicines/monographs/<generic-name>.md`.
