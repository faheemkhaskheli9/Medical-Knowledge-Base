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



## Checks
CI (`.github/workflows/docs.yml`, on pushes to `main` and on pull requests) runs both of these; run them locally before committing:

```sh
pip install -r requirements-docs.txt
python evals/check_evals.py   # evals YAML parses; case ids unique; every `source` file exists
mkdocs build --strict         # nav and internal links resolve
```

When adding a drug, also add a row to [`KB-INDEX.md`](KB-INDEX.md), an entry in the `mkdocs.yml` nav, and at least one case with a unique `id` in [`evals/medical-qa.yaml`](evals/medical-qa.yaml).
