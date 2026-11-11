#!/usr/bin/env python3
"""Additional order-144 construction upper bounds from order-36 direct factors."""
import json
from pathlib import Path

import order36_exhaustive as base36
from composite_constructions import AbstractGroup, abelian_group, solve

ROOT = Path(__file__).resolve().parent
PATHS = {
    3: "1/C3.A4.html",
    9: "1/C3^2sC4.html",
    10: "1/S3^2.html",
    11: "1/C3xA4.html",
    13: "1/C2xC3sS3.html",
    14: "1/C6^2.html",
}


def as_abstract(g):
    def mul(a, b):
        return base36.compose(a, b)
    return AbstractGroup(g["structure"], 6, g["identity"], mul, g["elements"])


def direct_product(name, a, b):
    identity = (a.identity, b.identity)
    def mul(x, y):
        return a.mul(x[0], y[0]), b.mul(x[1], y[1])
    elements = [identity] + [(x, y) for x in a.elements for y in b.elements if (x, y) != identity]
    return AbstractGroup(name, 12, identity, mul, elements)


def main():
    factors = [abelian_group("C4", 2, [4]), abelian_group("C2^2", 2, [2, 2])]
    results = []
    for gid, path in PATHS.items():
        a = as_abstract(base36.reconstruct(path))
        for b in factors:
            group = direct_product(f"SmallGroup(36,{gid}) [{a.name}] x {b.name}", a, b)
            rec = solve(group, 90)
            rec["order36_factor_id"] = gid
            results.append(rec)
            print(json.dumps(rec, ensure_ascii=False), flush=True)
    finite = [r["m"] for r in results if r["m"] is not None]
    summary = {"n": 12, "construction_upper_bound": min(finite),
               "universal_lower_bound": 13, "exact_global": min(finite) == 13,
               "best": [[r["structure"], r["subgroup_count"], r["status"]]
                        for r in results if r["m"] == min(finite)]}
    (ROOT / "order144_product_results.json").write_text(
        json.dumps({"summary": summary, "groups": results}, indent=2, ensure_ascii=False), encoding="utf-8")
    print("SUMMARY " + json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
