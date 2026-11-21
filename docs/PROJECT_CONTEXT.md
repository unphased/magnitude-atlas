# Magnitude Atlas — project context

## Purpose
Develop an auditable, spreadsheet-first atlas of enormous finite quantities, ordinal indices, and rigorous comparisons, later used for interactive charts, shader magnitude landscapes, and mathematical exploration.

## Current artifacts
- `magnitude_atlas_v03.xlsx`: current main workbook (v0.3, 23 sheets, reported 516 quantity records, 342 claims, 42 relations, 43 symbolic traces).
- `magnitude_atlas_v03_manifest.json`: machine-readable v0.3 data.
- `magnitude_atlas_starter/`: original v0.1 Python prototype, JSON data, tests, and instructions. THIS CODE PRECEDES v0.3 and does not implement all v0.3 features.

## Mathematical conventions discussed
- F_0(n) = n+1.
- F_(alpha+1)(n) = n-fold composition of F_alpha, starting from n.
- F_lambda(n) = F_(lambda[n])(n) for a declared fundamental sequence lambda[n].
- omega[n] = n; (omega*2)[n] = omega+n; (omega^2)[n] = omega*n; (omega^omega)[n] = omega^n.
- epsilon_0[n] = n-high finite tower of omegas for n>=1 (this choice is not universal).
- Some explorations used gamma_0[0]=0, gamma_0[k+1]=phi_(gamma_0[k])(0), gamma_0[n]=gamma_n; validate against chosen Veblen conventions before relying on recorded identities.
- Knuth up-arrow operations on natural numbers; Q = 10^100 is our googol base, and C_k = Q up-arrow^k Q are independent reference candles.

## Design principles
- Spreadsheet as approachable source of curated knowledge, rather than requiring all values to fit a single number type.
- Each quantity may have multiple equivalent exact symbolic forms, bounds, approximations, coordinate transforms, and linked derivations.
- Separate certified/proven statements from heuristic estimates and unknowns; don't infer output inequality merely from ordinal index ordering at small fixed arguments.
- Prefer lazy symbolic DAGs or iteration nodes (`Repeat`) for intractable FGH expressions; don't attempt to materialize enormous outputs.
- Possible visualizations: FGH n/index grid, googol-arrow count/argument surfaces, hyperlog/log-stack magnitude coordinates, ordinal staircase navigator, endless zoom with shader treatment.

## Research and review cautions
- The original Python code is a limited proof of concept and may be inefficient on integers with succinct exact formulas. Validate values and proofs before upgrading evidence labels.
- Explicit fundamental sequences matter: small-argument identities depend on exact choices, and expressions involving higher Veblen ordinals require a complete ordinal convention.
- The v0.3 workbook and manifest were generated in earlier conversation turns; treat their contents as working research data, not a formally verified mathematical database.

## Suggested next task
Audit the v0.3 symbolic claims for correctness, build a richer proof/derivation linkage model, and add higher ordinal/FHG and Knuth benchmark relationships without compromising provenance.
