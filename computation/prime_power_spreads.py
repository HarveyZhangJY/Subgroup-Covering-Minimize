#!/usr/bin/env python3
"""Certified n+1 subgroup spreads for n=2,3,4,5,7,8,9.

G = F_q^2 as an additive group, q=n. The q one-dimensional F_q-subspaces
together with the vertical line give q+1 additive subgroups of order q.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARAMS = {
    2: (2, 1, [1, 1], [4, 2], "C2^2"),
    3: (3, 1, [1, 0], [9, 2], "C3^2"),
    4: (2, 2, [1, 1, 0], [16, 14], "C2^4"),       # x^2+x+1, x^2=x+1
    5: (5, 1, [1, 0], [25, 2], "C5^2"),
    7: (7, 1, [1, 0], [49, 2], "C7^2"),
    8: (2, 3, [1, 1, 0, 0], [64, 267], "C2^6"),  # x^3+x+1, x^3=x+1
    9: (3, 2, [2, 0], [81, 15], "C3^4"),         # x^2+1, x^2=2
}


def coefficients(a, p, k):
    return [(a // (p**i)) % p for i in range(k)]


def encode(c, p):
    return sum(x * p**i for i, x in enumerate(c))


def add(a, b, p, k):
    aa, bb = coefficients(a, p, k), coefficients(b, p, k)
    return encode([(x+y) % p for x, y in zip(aa, bb)], p)


def mul(a, b, p, k, reduction):
    if k == 1:
        return (a*b) % p
    aa, bb = coefficients(a, p, k), coefficients(b, p, k)
    product = [0] * (2*k-1)
    for i, x in enumerate(aa):
        for j, y in enumerate(bb):
            product[i+j] = (product[i+j] + x*y) % p
    # x^k = reduction[0] + ... + reduction[k-1]x^(k-1).
    for d in range(2*k-2, k-1, -1):
        coeff = product[d] % p
        for j in range(k):
            product[d-k+j] = (product[d-k+j] + coeff*reduction[j]) % p
    return encode(product[:k], p)


def inverse(a, p, k, reduction):
    assert a
    for b in range(1, p**k):
        if mul(a, b, p, k, reduction) == 1:
            return b
    raise ValueError("polynomial is not irreducible")


def solve(n):
    p, k, reduction, gid, structure = PARAMS[n]
    q = p**k
    assert q == n
    elements = [(a, b) for a in range(q) for b in range(q)]
    # Verify field arithmetic, hence the line construction.
    for a in range(1, q):
        inverse(a, p, k, reduction)
    lines = []
    labels = []
    for c in range(q):
        H = {(a, mul(c, a, p, k, reduction)) for a in range(q)}
        lines.append(H)
        labels.append(f"slope {c}")
    lines.append({(0, b) for b in range(q)})
    labels.append("vertical")
    assert len(lines) == n+1
    union = set().union(*lines)
    assert union == set(elements)
    for i, H in enumerate(lines):
        assert len(H) == n and (0, 0) in H
        for a in H:
            for b in H:
                assert (add(a[0], b[0], p, k), add(a[1], b[1], p, k)) in H
        for H2 in lines[:i]:
            assert H.intersection(H2) == {(0, 0)}
    pos = {x: i for i, x in enumerate(elements)}
    masks = [sum(1 << pos[x] for x in H) for H in lines]
    total_subspaces = 1
    numerator, denominator = 1, 1
    for i in range(k):
        numerator *= p**(2*k-i)-1
        denominator *= p**(k-i)-1
    total_subspaces = numerator // denominator
    return {
        "n": n, "order": n*n, "smallgroup_id": gid, "structure": structure,
        "minimum_m": n+1, "exact": True,
        "proof": "universal counting lower bound n+1 plus a finite-field 1-spread",
        "subgroup_count_in_witness_group": total_subspaces,
        "subgroups_used": n+1,
        "note": "The witness uses n+1 F_n-lines; subgroup_count_in_witness_group counts all F_p-rational k-subspaces.",
        "labels": labels,
        "subgroups": [sorted(H) for H in lines],
        "witness_masks": [str(m) for m in masks],
        "covered_elements": len(union), "union_equals_group": True,
        "pairwise_intersection_identity": True,
    }


def main():
    results = [solve(n) for n in PARAMS]
    (ROOT / "prime_power_results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    for r in results:
        print({k: r[k] for k in ("n", "smallgroup_id", "structure", "minimum_m", "subgroup_count_in_witness_group", "covered_elements")})


if __name__ == "__main__":
    main()
