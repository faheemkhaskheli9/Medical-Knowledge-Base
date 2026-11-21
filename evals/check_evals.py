#!/usr/bin/env python3
"""Validate medical evaluation YAML cases before publishing.

Usage: python evals/check_evals.py

Validation covers required fields, duplicate identifiers, nonempty expected phrases,
source containment within the repository, and malformed YAML types.
"""
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
EVALS = ROOT / "evals"
REQUIRED = ("id", "question", "audience", "must_include", "source")

class UniqueKeySafeLoader(yaml.SafeLoader):
    """Reject duplicate YAML mapping keys rather than silently accepting the last value."""


def _construct_unique_mapping(loader, node):
    loader.flatten_mapping(node)
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=True)
        try:
            if key in seen:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate YAML key {key!r}", key_node.start_mark
                )
            seen.add(key)
        except TypeError as exc:
            raise yaml.constructor.ConstructorError(
                None, None, "unhashable YAML mapping key", key_node.start_mark
            ) from exc
    return loader.construct_mapping(node)


UniqueKeySafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_unique_mapping
)



def validate_case(case, where, seen, root=ROOT):
    """Return errors for one case; do not throw on malformed YAML values."""
    errors = []
    if not isinstance(case, dict):
        return [f"{where}: expected a mapping"]
    for key in ("id", "question", "audience", "source"):
        value = case.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{where}: '{key}' must be a non-empty string")
    for key in ("must_include", "must_not"):
        if key not in case and key == "must_not":
            continue
        value = case.get(key)
        if not isinstance(value, list) or (key == "must_include" and not value):
            errors.append(f"{where}: '{key}' must be {'a non-empty' if key == 'must_include' else 'a'} list")
        elif any(not isinstance(item, str) or not item.strip() for item in value):
            errors.append(f"{where}: '{key}' entries must be non-empty strings")
    audience = case.get("audience")
    if isinstance(audience, str) and audience.strip() and audience not in ("patient", "clinician"):
        errors.append(f"{where}: 'audience' must be 'patient' or 'clinician'")
    cid = case.get("id")
    if isinstance(cid, str) and cid.strip():
        if cid in seen:
            errors.append(f"{where}: duplicate id {cid!r} (first in {seen[cid]})")
        else:
            seen[cid] = where
    source = case.get("source")
    if isinstance(source, str) and source.strip():
        # Resolve symlinks and traversal before testing existence.
        source_path = Path(source)
        if source_path.is_absolute():
            errors.append(f"{where}: source must be relative to repository: {source}")
        else:
            root_resolved = root.resolve()
            target = (root_resolved / source_path).resolve()
            if not target.is_relative_to(root_resolved):
                errors.append(f"{where}: source must remain inside repository: {source}")
            elif not target.is_file():
                errors.append(f"{where}: source does not exist: {source}")
    return errors


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
            data = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeySafeLoader)
        except (yaml.YAMLError, UnicodeError, OSError) as exc:
            errors.append(f"{rel}: cannot read/parse YAML: {exc}")
            continue
        if not isinstance(data, list):
            errors.append(f"{rel}: expected a list of cases, got {type(data).__name__}")
            continue
        for i, case in enumerate(data):
            where = f"{rel}: case #{i + 1}"
            total += 1
            errors.extend(validate_case(case, where, seen))
    for err in errors:
        print(f"ERROR {err}", file=sys.stderr)
    if errors:
        print(f"{len(errors)} error(s) in {len(files)} file(s)", file=sys.stderr)
        return 1
    print(f"OK: {total} cases in {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
