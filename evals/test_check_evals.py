"""Regression coverage for medical evaluation schema and source confinement."""
import tempfile
import unittest
from pathlib import Path

import yaml

from check_evals import UniqueKeySafeLoader, validate_case


class EvalCaseValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo"
        self.root.mkdir()
        (self.root / "source.md").write_text("Reference", encoding="utf-8")
        self.valid = {
            "id": "case-1", "question": "What is the evidence?",
            "audience": "clinician", "must_include": ["evidence"],
            "source": "source.md",
        }

    def check(self, case, seen=None):
        return validate_case(case, "test-case", {} if seen is None else seen, root=self.root)

    def test_valid_case(self):
        self.assertEqual(self.check(self.valid), [])

    def test_non_mapping_case(self):
        self.assertIn("expected a mapping", " ".join(self.check(None)))

    def test_required_fields_and_phrase_types(self):
        for key, value in (("id", 4), ("question", " "), ("audience", None),
                           ("source", []), ("must_include", []),
                           ("must_include", [" "]), ("must_not", [None])):
            with self.subTest(key=key, value=value):
                self.assertTrue(self.check({**self.valid, key: value}))

    def test_audience_restricted_to_supported_roles(self):
        for audience in ("patient", "clinician"):
            with self.subTest(audience=audience):
                self.assertEqual(self.check({**self.valid, "audience": audience}), [])
        for audience in ("visitor", "Patient", "patient ", "clinicians"):
            with self.subTest(audience=audience):
                self.assertIn("must be 'patient' or 'clinician'",
                              " ".join(self.check({**self.valid, "audience": audience})))

    def test_optional_empty_must_not(self):
        self.assertEqual(self.check({**self.valid, "must_not": []}), [])

    def test_duplicate_identifier_across_cases(self):
        seen = {}
        self.assertEqual(self.check(self.valid, seen), [])
        self.assertIn("duplicate id", " ".join(self.check(self.valid, seen)))

    def test_missing_source(self):
        self.assertIn("does not exist", " ".join(self.check({**self.valid, "source": "missing.md"})))

    def test_absolute_source_inside_repository_is_rejected(self):
        self.assertIn("must be relative", " ".join(self.check({**self.valid, "source": str(self.root / "source.md")})))

    def test_parent_traversal_is_rejected(self):
        self.assertIn("inside repository", " ".join(self.check({**self.valid, "source": "../outside.md"})))

    def test_symlink_escape_is_rejected(self):
        outside = Path(self.temp.name) / "outside.md"
        outside.write_text("private", encoding="utf-8")
        try:
            (self.root / "link.md").symlink_to(outside)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unsupported")
        self.assertIn("inside repository", " ".join(self.check({**self.valid, "source": "link.md"})))


class DuplicateYamlKeyTests(unittest.TestCase):
    def test_valid_mapping(self):
        self.assertEqual(yaml.load("a: 1\nb: 2\n", Loader=UniqueKeySafeLoader), {"a": 1, "b": 2})

    def test_duplicate_top_level_key(self):
        with self.assertRaisesRegex(yaml.YAMLError, "duplicate YAML key"):
            yaml.load("a: 1\na: 2\n", Loader=UniqueKeySafeLoader)

    def test_duplicate_nested_case_key(self):
        with self.assertRaisesRegex(yaml.YAMLError, "duplicate YAML key"):
            yaml.load("- id: first\n  source: a.md\n  source: b.md\n", Loader=UniqueKeySafeLoader)

    def test_same_key_in_distinct_cases(self):
        self.assertEqual(yaml.load("- id: one\n- id: two\n", Loader=UniqueKeySafeLoader),
                         [{"id": "one"}, {"id": "two"}])

    def test_unhashable_mapping_key(self):
        with self.assertRaises(yaml.YAMLError):
            yaml.load("? [a, b]\n: value\n", Loader=UniqueKeySafeLoader)


if __name__ == "__main__":
    unittest.main()
