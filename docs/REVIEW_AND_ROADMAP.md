# Initial audit and proposed improvements

## Inventory

- Workbook v0.3: 23 sheets, including Quantities, Claims, Relations, Derivations, Symbolic Traces, Rewrite Rules, Proof Targets and Compression Lab.
- Manifest v0.3: declared total counts 516 quantities, 342 claims, 42 relations, 25 proof records, 43 trace steps and 22 rewrite rules. Some arrays are additions relative to a prior workbook, **not necessarily full table exports**; do not infer that counts equal array lengths.
- Python v0.1: one dependency-free CLI, a finite FGH integer evaluator with call/bit budgets, an `omega` *summary*, and an `F_3` logarithmic heuristic. Three small JSON files and five existing `unittest` tests.

## Limitations / risks

1. The v0.1 engine does not parse or evaluate general transfinite ordinal expressions; its `omega` path only emits the `F_n(n)` reduction.
2. The evaluator's call and bit budgets are essential for termination, but its recursive implementation is not optimized for algebraically succinct huge outputs; Python recursion limits can occur.
3. `f3_residue_heuristic` is **not certified interval arithmetic**. The existing numerical tests check repeatability, not rigor.
4. `derived.json` in the old prototype and the v0.3 manifest are different generations of research data. Do not merge them or claim they synchronize automatically.
5. Provenance/status semantics and Veblen/fundamental-sequence choices need a schema and independent review before expanding the proof system.

## Suggested order of work (not yet implemented)

1. Add non-destructive catalog validation: stable IDs, references, evidence/status types, and cross-links to claims/derivations.
2. Add small exact FGH and ordinal fundamental-sequence regression vectors; document the indexing used in each reduction.
3. Introduce a typed, lazy expression DAG (`Number`, `FCall`, `HyperOp`, `Repeat`, `Power`) without eager huge expansions.
4. Add conservative symbolic comparison (`LT`, `GT`, `EQ`, `UNKNOWN`) accompanied by checkable proof traces.
5. Explore certified interval/log-stack coordinates separately from existing heuristics; only then link engine outputs back to workbook research.

No original mathematical engine implementation was modified in repository initialization.
