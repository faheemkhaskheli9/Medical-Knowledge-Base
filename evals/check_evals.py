#!/usr/bin/env python3
"""Validate the evaluation set.

Loads every evals/*.yaml / *.yml file and fails (exit 1) on:
- YAML parse errors, or a file that is not a list of cases
- cases missing a required field (id, question, audience, must_include, source)
- duplicate case ids (across all files)
- `source` paths that do not exist (relative to the repository root)

Usage: python evals/check_evals.py
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
REQUIRED = ("id", "question", "audience", "must_include", "source")


def main() -> int:
    errors = []
    seen = {}
    files = sorted(list(EVALS.glob("*.yaml")) + list(EVALS.glob("*.yml")))
    if not files:
        errors.append("no eval YAML files found in evals/")
    total = 0
    for path in files:
        rel = path.relative_to(ROOT)
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{rel}: YAML parse error: {exc}")
            continue
        if not isinstance(data, list):
            errors.append(f"{rel}: expected a list of cases, got {type(data).__name__}")
            continue
        for i, case in enumerate(data):
            where = f"{rel}: case #{i + 1}"
            if not isinstance(case, dict):
                errors.append(f"{where}: expected a mapping")
                continue
            total += 1
            cid = case.get("id")
            if cid is not None:
                where = f"{rel}: {cid}"
            for key in REQUIRED:
                if not case.get(key):
                    errors.append(f"{where}: missing or empty '{key}'")
            for key in ("must_include", "must_not"):
                if key in case and not isinstance(case[key], list):
                    errors.append(f"{where}: '{key}' must be a list")
            if cid is not None:
                if cid in seen:
                    errors.append(f"{where}: duplicate id (first in {seen[cid]})")
                else:
                    seen[cid] = rel
            src = case.get("source")
            if isinstance(src, str) and src and not (ROOT / src).is_file():
                errors.append(f"{where}: source does not exist: {src}")
    for err in errors:
        print(f"ERROR {err}", file=sys.stderr)
    if errors:
        print(f"{len(errors)} error(s) in {len(files)} file(s)", file=sys.stderr)
        return 1
    print(f"OK: {total} cases in {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
