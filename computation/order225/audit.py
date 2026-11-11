#!/usr/bin/env python3
"""Offline consistency, coverage, forcing, and optimality audit for order 225."""
import csv
import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ORDER = 225
N = 15
FULL = set(range(ORDER))

for name in ("covers-15.jsonl", "solutions-15.jsonl", "classification-225.tsv", "export-15.log"):
    digest = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    print(f"SHA256 {name}: {digest}")

with (ROOT / "classification-225.tsv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))
assert [int(row["id"]) for row in rows] == list(range(1, 7))
classes = {int(row["id"]): row for row in rows}
for i, row in classes.items():
    assert int(row["exp"]) in (15, 45, 75, 225)
    assert int(row["H15"]) >= 0
excluded = {i for i, row in classes.items() if N % int(row["exp"]) != 0}
eligible = set(classes) - excluded
assert excluded == {1, 2, 3, 4} and eligible == {5, 6}
assert [int(classes[i]["H15"]) for i in range(1, 7)] == [1, 4, 6, 6, 6, 24]

log_text = (ROOT / "export-15.log").read_text(encoding="utf-8", errors="replace")
assert "order=225; groups=6" in log_text
assert "finished all 6 groups of order 225" in log_text
logged_ids = [int(x) for x in re.findall(r"^done 225 (\d+) ", log_text, re.MULTILINE)]
assert logged_ids == list(range(1, 7))

cover_list = [json.loads(line) for line in (ROOT / "covers-15.jsonl").read_text().splitlines() if line.strip()]
covers = {record["id"]: record for record in cover_list}
assert len(cover_list) == len(covers) == 6 and set(covers) == set(classes)
for i, record in covers.items():
    assert record["exp"] == int(classes[i]["exp"])
    assert len(record["subs"]) == int(classes[i]["H15"])
    identity = record["identity_index"]
    normalized = []
    for sub in record["subs"]:
        assert len(sub) == len(set(sub)) == N
        assert identity in sub
        assert all(type(e) is int and 0 <= e < ORDER for e in sub)
        normalized.append(tuple(sorted(sub)))
    assert len(set(normalized)) == len(normalized)

solution_list = [json.loads(line) for line in (ROOT / "solutions-15.jsonl").read_text().splitlines() if line.strip()]
solutions = {record["id"]: record for record in solution_list}
assert len(solution_list) == len(solutions) == 6 and set(solutions) == set(classes)
for i, solution in solutions.items():
    assert solution["variables"] == len(covers[i]["subs"])
    counts = Counter(e for sub in covers[i]["subs"] for e in sub)
    union = set(counts)
    forced = [j for j, sub in enumerate(covers[i]["subs"]) if any(counts[e] == 1 for e in sub)]
    assert solution["forced_subgroups"] == forced
    assert solution["union_size"] == len(union)
    assert solution["uncovered_count"] == ORDER - len(union)
    if union != FULL:
        assert solution["status"] == "no_cover" and solution["cover"] is None
    else:
        assert solution["status"] == "optimal" and solution["solver_status"] == 0
        selected = solution["selected"]
        assert len(selected) == len(set(selected)) == solution["cover"]
        assert set().union(*(set(covers[i]["subs"][j]) for j in selected)) == FULL
        assert math.isclose(solution["bound"], solution["cover"], abs_tol=1e-9)
        assert set(forced) <= set(selected)

assert all(solutions[i]["status"] == "no_cover" for i in range(1, 6))
assert [solutions[i]["union_size"] for i in range(1, 6)] == [15, 45, 75, 75, 75]
assert solutions[5]["union_size"] == 75 and solutions[5]["uncovered_count"] == 150
assert solutions[6]["cover"] == 24 and solutions[6]["bound"] == 24.0
assert solutions[6]["selected"] == list(range(24))
assert solutions[6]["forced_subgroups"] == list(range(24))
assert len(covers[6]["subs"]) == 24
assert set().union(*(set(s) for s in covers[6]["subs"])) == FULL

print("Classification: 6/6 groups; all order-15 subgroups exported for every group")
print("Exponent-excluded=[1,2,3,4]; exponent-eligible=[5,6]")
print("SmallGroup(225,1..5): no cover; subgroup unions=15,45,75,75,75 out of 225")
print("SmallGroup(225,5): 6 subgroups, union=75/225, no cover")
print("SmallGroup(225,6): 24 subgroups, all forced by private elements, union=225/225")
print("MILP: status=optimal, cover=24, dual_bound=24, selected=0..23")
print("AUDIT RESULT: PASS; complete order-225 enumeration proves alpha(15)=24")
