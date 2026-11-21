#!/usr/bin/env python3
"""Magnitude Atlas v0.1: intentionally small, deterministic CLI. No dependencies."""
import argparse
import json
from decimal import Decimal, localcontext
from math import factorial
from pathlib import Path

CATALOG = Path(__file__).resolve().parent / "data/catalog.json"
RELATIONS = Path(__file__).resolve().parent / "data/relations.json"

class BudgetExceeded(Exception):
    pass

def f_exact(level: int, n: int, *, max_bits: int = 100_000, max_calls: int = 100_000) -> int:
    """Evaluate finite FGH with strict budgets; avoid huge exponent allocations."""
    calls = [0]
    def rec(k, x):
        calls[0] += 1
        if calls[0] > max_calls or x.bit_length() > max_bits:
            raise BudgetExceeded("call or integer-size budget reached")
        if k == 0:
            return x + 1
        if x > max_calls - calls[0]:
            raise BudgetExceeded("iteration count exceeds call budget")
        value = x
        for _ in range(x):
            value = rec(k - 1, value)
        return value
    if level < 0 or n < 0:
        raise ValueError("level and argument must be nonnegative")
    return rec(level, n)

def f3_residue_heuristic(n: int, digits: int = 44) -> dict:
    """Estimate L_n(F3(n)) without expanding huge numbers.

    This is a scale approximation, NOT a certified interval or original-number
    mantissa. For n>=3 and growing n, discarded corrections shrink rapidly.
    """
    if n < 3 or n > 10000:
        raise ValueError("demo supports F3 arguments 3..10000")
    with localcontext() as ctx:
        ctx.prec = digits
        a = Decimal(2).log10()
        x1 = n * (1 << n)   # first g application; modest in memory
        log_x1 = Decimal(x1).log10()
        log_x2 = Decimal(x1)*a + log_x1  # mathematically exact expression
        # The 'a' term is a strong asymptotic reduction for all later steps.
        r = (log_x2 + a.log10()).log10()
        return {
            "status": "heuristic",
            "measure": f"L_{n}(F_3({n}))",
            "log_base": 10,
            "iterations": n,
            "residue_estimate": format(r, '.14f'),
            "method": "first-step exact + asymptotic logarithmic cancellation",
            "warning": "Not an error-certified interval, nor the mantissa of F_3(n)."
        }

def summarize(level: str, n: int) -> dict:
    if n < 0:
        raise ValueError("argument must be nonnegative")
    if level.lower() == "omega":
        return {"definition": f"F_omega({n})", "reduction": f"F_{n}({n})", "status":"exact"}
    k = int(level)
    result = {"definition":f"F_{k}({n})", "expansion":f"iterate(F_{k-1}, start={n}, count={n})" if k>0 else f"{n}+1"}
    try:
        exact = f_exact(k, n, max_bits=100_000, max_calls=100_000)
        result.update(status="exact", value=str(exact) if exact.bit_length() <= 1000 else f"({exact.bit_length()}-bit integer; output suppressed)", bits=exact.bit_length())
    except (BudgetExceeded, RecursionError):
        result.update(status="symbolic", note="Exact evaluation exceeds configured budget")
    if k == 3 and 3 <= n <= 10000:
        result["log_estimate"] = f3_residue_heuristic(n)
    elif k == 4 and n == 2:
        result["reduction"] = "F_3(2048)"
        result["log_estimate"] = f3_residue_heuristic(2048)
    return result

def export():
    catalog = json.loads(CATALOG.read_text())
    derived = [summarize(str(k), n) for k,n in [(2,3), (3,2), (3,3), (3,5), (3,6), (3,50), (4,2)]]
    return {"source_catalog_version":catalog["schema_version"], "derived":derived, "bounds":json.loads(RELATIONS.read_text())["relations"]}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    s=p.add_subparsers(dest="command", required=True)
    s.add_parser("catalog", help="Print landmark catalog")
    f=s.add_parser("f", help="Summarize a finite-level or omega FGH call")
    f.add_argument("level", help="nonnegative integer or omega")
    f.add_argument("argument", type=int)
    s.add_parser("export", help="Export replaceable derived estimates as JSON")
    args=p.parse_args()
    if args.command=="catalog":
        for e in json.loads(CATALOG.read_text())["entries"]:
            print(f"{e['id']:22} {e['expression']}")
    elif args.command=="f":
        print(json.dumps(summarize(args.level, args.argument), indent=2, ensure_ascii=False))
    else:
        print(json.dumps(export(), indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
