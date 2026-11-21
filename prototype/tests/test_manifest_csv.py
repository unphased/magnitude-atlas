"""Validate the v0.3 UTF-8 CSV exports against the archived JSON manifest."""
import csv
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "research/v0.3/magnitude_atlas_v03_manifest.json"
CSV_DIR = MANIFEST.parent / "csv"
TABLES = (
    "new_quantities", "new_claims", "new_relations", "new_derivations",
    "symbolic_traces", "rewrite_rules", "compression_lab", "proof_targets",
)

def to_cell(value):
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return str(value)

class ManifestCSVTests(unittest.TestCase):
    def test_csv_tables_match_manifest(self):
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        for table in TABLES:
            with self.subTest(table=table):
                records = manifest[table]
                columns = list(dict.fromkeys(key for row in records for key in row))
                with (CSV_DIR / (table + ".csv")).open(
                    "r", encoding="utf-8", newline=""
                ) as file:
                    reader = csv.DictReader(file)
                    self.assertEqual(reader.fieldnames, columns)
                    actual = list(reader)
                self.assertEqual(len(actual), len(records))
                for index, (got, original) in enumerate(zip(actual, records)):
                    self.assertEqual(
                        got,
                        {column: to_cell(original.get(column)) for column in columns},
                        f"{table} row {index}",
                    )

if __name__ == "__main__":
    unittest.main()
