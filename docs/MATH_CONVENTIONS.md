# Mathematical conventions (preserved from supplied project)

The following are project-specific definitions. Never silently replace these with conventions from another author.

- `F_0(n) = n + 1`.
- `F_(α+1)(n)` is **n** compositions of `F_α`, with initial value **n**.
- `F_λ(n) = F_(λ[n])(n)` for limits and explicitly declared fundamental sequences.
- `ω[n] = n`; `(ω·2)[n] = ω+n`; `(ω²)[n] = ω·n`; `(ω^ω)[n] = ω^n`.
- For ε₀: `t_0=1`, `t_(n+1)=ω^(t_n)`, and `ε₀[n]=t_n`, yielding an n-high tower of ω for n≥1. Different treatments may choose different indexing.
- A prior exploratory γ₀ sequence uses `γ_0[0]=0`, `γ_0[k+1]=φ_(γ_0[k])(0)` and `γ_0[n]=γ_n`. **Veblen notation and this identity still require validation** before being trusted or implemented.
- Knuth up arrows act on natural numbers; `Q=10^100`, and `C_k=Q ↑^k Q` are independent reference candles.
- `L_k(x)` means applying `log10` k times; this is not `(log10(x))^k`. Approximate `L_k` coordinates do not identify the original number's mantissa.

Evidence classes appearing in research: `exact`, `exact symbolic`, `convention-dependent`, `proved_bound`, `heuristic`, `approximate`, `unknown`. Do not promote a heuristic or an unverified relation into a proof. An ordinal index inequality alone does not establish fixed-small-input FGH inequality.
