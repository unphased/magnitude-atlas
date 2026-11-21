# Magnitude Atlas

An auditable, spreadsheet-first research atlas of enormous finite numbers, fast-growing hierarchies, ordinal indices, and symbolic comparisons.

## Project boundaries

- **Research catalog:** [`research/v0.3/magnitude_atlas_v03.xlsx`](research/v0.3/magnitude_atlas_v03.xlsx) is the current curated, human-facing workbook (23 sheets). Its companion JSON manifest is a preserved snapshot of the v0.3 research, **not** a verified export produced by the v0.1 engine.
- **Code:** [`prototype/`](prototype/) contains the **original v0.1 Python prototype**, preserved without algorithmic changes. GitHub should be authoritative for code and tests, not for mathematical assertions independently of review.
- **Conventions:** [`docs/MATH_CONVENTIONS.md`](docs/MATH_CONVENTIONS.md) records the definitions and unresolved convention questions.
- **Limitations:** [`docs/REVIEW_AND_ROADMAP.md`](docs/REVIEW_AND_ROADMAP.md) separates current capabilities from proposed improvements.

## Run existing code and tests

Requires Python 3.11+ and no external dependencies.

```bash
python3 prototype/atlas.py f 3 2
python3 -m unittest discover -s prototype/tests -v
```

The code is intentionally *not* described as a v0.3 engine. In particular, higher ordinal expressions and most catalog research are not executable by this prototype.

## Workflow

Edit and curate research in the workbook. Commit snapshots of the workbook and its manifest together when appropriate. Make code changes through Git commits and tests; do not regenerate or overwrite the workbook from v0.1 `export`. Research statements must retain provenance and evidence status. See [`docs/PROJECT_CONTEXT.md`](docs/PROJECT_CONTEXT.md).

## GitHub execution and CI

The [Magnitude Atlas CI workflow](../../actions/workflows/tests.yml) runs automatically on pushes and pull requests. To run it on demand, open **Actions → Magnitude Atlas CI → Run workflow** (choose `main`). The job compiles Python, runs the five prototype tests, validates JSON, and runs the CLI.

Click a workflow run → **test-and-demo** to see the individual steps and stdout. Under **Artifacts**, download `atlas-cli-output` to inspect `catalog.txt`, `f3-2.json`, `fomega-5.json`, and `export.json`. These are reproducible example executions, not formal proof certificates.

The workflow uses only the standard library and does not modify the research workbook.
