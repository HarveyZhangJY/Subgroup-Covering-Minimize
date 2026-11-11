#!/usr/bin/env python3
"""Independently recheck every saved witness mask and print the experiment table."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def check_record(rec, n):
    masks = [int(x) for x in rec["witness_masks"]]
    expected = rec.get("minimum_m", rec.get("m"))
    assert len(masks) == expected
    assert all(m.bit_count() == n for m in masks)
    union = 0
    for m in masks:
        union |= m
    assert union == (1 << (n*n))-1
    assert union.bit_count() == n*n


def main():
    prime = json.loads((ROOT/"prime_power_results.json").read_text())
    for r in prime:
        check_record(r, r["n"])
        assert r["minimum_m"] == r["n"]+1
    o36 = json.loads((ROOT/"order36_results.json").read_text())
    for r in o36["groups"]:
        if r["m"] is not None:
            check_record(r, 6)
            assert r["status"] == "optimal" and r["lower_bound"] == r["m"]
    assert o36["summary"]["minimum_m"] == 10 and o36["summary"]["exact"]
    comp = json.loads((ROOT/"composite_results.json").read_text())
    for r in comp["order100"]["groups"]:
        check_record(r, 10)
        assert r["status"] == "optimal" and r["lower_bound"] == r["m"]
    assert comp["order100"]["summary"]["minimum_m"] == 16
    for r in comp["order144"]["groups"]:
        check_record(r, 12)
    product_path = ROOT/"order144_product_results.json"
    if product_path.exists():
        products = json.loads(product_path.read_text())
        for r in products["groups"]:
            if r["m"] is not None:
                check_record(r, 12)
    print("All saved witnesses pass: subgroup sizes, m, and full-group union.")
    values = {r["n"]: r["minimum_m"] for r in prime}
    values.update({6: 10, 10: 16})
    print("n=2..10 exact values:", [values[n] for n in range(2, 11)])
    print("n=12: M(12) = 17 (complete 197-group certificate; verified by order144/audit.py)")


if __name__ == "__main__":
    main()
