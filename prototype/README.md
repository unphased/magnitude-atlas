# Magnitude Atlas — starter project (v0.1)

A **math-first, visualization-agnostic catalog** of huge numbers and comparison landmarks.
Its job is to answer: *what exactly is this quantity, what do we actually know about
its magnitude, and can that claim be checked?*

The long-term goal is to drive interactive FGH grids, Knuth-arrow reference surfaces,
log-stack/super-log axes, and Mandelbrot-like magnitude zooms from **one auditable library**.
The renderer should never need to invent numerical claims.

## Run

Requires Python 3.11+; no third-party packages.

```bash
python3 atlas.py catalog
python3 atlas.py f 3 5
python3 atlas.py f 3 50
python3 atlas.py f 4 2
python3 atlas.py f omega 5
python3 atlas.py export > data/derived.json
python3 -m unittest discover -s tests -v
```

## Rules and conventions (do not silently change)

- **FGH**: `F_0(n)=n+1`; `F_(k+1)(n)` applies `F_k` exactly `n` times,
  starting from `n`. For the first limit, `F_omega(n)=F_n(n)`.
  These conventions differ across publications. Future ordinal extensions must
  declare their fundamental-sequence policy.
- **Knuth arrows**: one arrow = exponentiation; two arrows = tetration.
- `Q = 10^100` is the googol; `Q ↑^k Q` is a candidate candle family.
- `L_k(x) = log10` composed `k` times. `L_k` is **not** `(log10 x)^k`.
- **Physical estimates** carry units, date/definition, and an evidence URL.
- Do not conflate exact definitions, certified bounds, approximate measurements,
  and heuristic compression estimates.

## Confidence/status fields

| Status | Meaning |
|---|---|
| `exact` | Symbolic identity or exact integer with a reproducible derivation |
| `proved_bound` | Explicit mathematical inequality with stated assumptions |
| `approximate` | Rounded scientific/observational quantity with source |
| `heuristic` | Numerical estimate without a proved error interval; not a certified bound |
| `unknown` | We do not yet have a useful bound or evaluator |

**Important:** Small errors in a *deeply compressed* logarithmic residue can
translate into enormous differences in the reconstructed number. The `f3`
residue routine is deliberately labeled `heuristic` until interval-based
certification is implemented. These residues describe scale, NOT the leading
decimal digits of the original number.

## Data model and development plan

`data/catalog.json` is the stable, hand-reviewed source of *definitions and
landmarks*. `data/relations.json` contains proved orderings that the UI can
display without guessing. `atlas.py export` produces replaceable derived metrics for the UI.
Each item has a stable ID, expression, definitions, and claims with explicit
statuses and sources. Exact integers are stored as strings; enormous numbers
remain symbolic.

Next milestones:

1. Add a typed, hash-consed expression DAG: `Number`, `Power`, `FCall`,
   `HyperOp`, `Iterate` (with symbolic `count`). Provide *virtual* pagination,
   not eager unrolling.
2. Add **interval arithmetic** and independently verified reduction rules for
   iterated-log coordinates. Track error *through* transformations.
3. Add an order/bounds prover that returns `LT`, `GT`, `EQ`, or `UNKNOWN` with a
   proof trace, never inventing a rank when unable to compare.
4. Generate a reusable FGH-by-argument matrix and Q-arrow reference matrix
   with typed cells: exact / proved interval / heuristic / unresolved.
5. **Then** try rendering: logarithmic, log-depth + residue, continuous super-log
   approximations (with the definition chosen explicitly), and shader zoom.

### Design rule

**The catalog is the scientific instrument; visualizations are consumers.**
Version conventions, store provenance, preserve unknowns, and regression-test
reference cells before adding pretty plots.

## References

- FGH definition/conventions: https://graphsearch.epfl.ch/en/concept/24947285
- Further mathematical context: https://neugierde.github.io/cantors-attic/Fast-growing_hierarchy
- Inverse Ackermann discussion: https://www.gabrielnivasch.org/fun/inverse-ackermann
- NASA, observable-universe diameter ~92 billion ly:
  https://www.nasa.gov/science-research/astrophysics/how-big-is-space-we-asked-a-nasa-expert-episode-61/
- NASA, Andromeda ~2.5 million ly: https://www.nasa.gov/universe/galaxies/andromeda-galaxy/
- NASA, Proxima ~4.25 ly: https://imagine.gsfc.nasa.gov/features/cosmic/nearest_star_info.html

## Numerical audit note

Use `L_n(F_3(n))` for the n-fold logarithmic compression of `F_3(n)`;
earlier conversational examples occasionally mixed up the log count. For
example, `L_5(F_3(5))` is about 1.698, **not** `L_4(F_3(5))`.
Derived values are intentionally replaceable outputs, not fixed axioms.
