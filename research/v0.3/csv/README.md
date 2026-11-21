# v0.3 research archive: CSV export scope

The JSON manifest is preserved at `../magnitude_atlas_v03_manifest.json`. Its eight array sections were exported **losslessly as UTF-8 CSV** here, with every value quoted, standard doubled-quote escaping, and the union of record keys as column headers.

| CSV | Records |
|---|---:|
| `new_quantities.csv` | 377 |
| `new_claims.csv` | 194 |
| `new_relations.csv` | 14 |
| `new_derivations.csv` | 10 |
| `symbolic_traces.csv` | 43 |
| `rewrite_rules.csv` | 22 |
| `compression_lab.csv` | 17 |
| `proof_targets.csv` | 10 |

**Total: 687 rows across these eight tables**, not 687 unique quantities.

Important: the original v0.3 workbook has **23 sheets**, and the manifest contains `new_*` additions rather than all workbook records. These CSVs are therefore **not a complete XLSX-to-CSV conversion** and must not be treated as a replacement for the original workbook. The workbook is retained in the downloadable repository archive but has not yet been committed to GitHub.

For nested objects, the CSV field contains compact JSON text. An empty CSV field represents a missing key or a JSON null. The manifest remains the canonical machine-readable source for these records; `prototype/tests/test_manifest_csv.py` checks row-by-row parity in CI.

To inspect with Python:
```python
import csv
with open("research/v0.3/csv/new_quantities.csv", encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f):
        print(row["id"], row["expression"])
        break
```
