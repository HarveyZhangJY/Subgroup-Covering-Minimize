#!/usr/bin/env python3
"""Offline audit for the n=18 computation.

Reads ONLY the saved files (covers-18.jsonl, solutions-18.jsonl,
export-18.log); does not rerun GAP or HiGHS. Checks:

  1. all 176 SmallGroup(324, i) ids are accounted for exactly once in
     export-18.log (either exponent-excluded or exported);
  2. exponent-excluded ids really satisfy 18 mod Exponent(G) != 0, and
     exported ids satisfy 18 | Exponent(G);
  3. every saved subgroup has size 18, indices in [0,324), contains 0, and
     the saved subgroup count matches the export log;
  4. each group is either reported non-coverable (with an actually
     incomplete union) or has a selected cover whose re-expanded union is
     exactly 324/324 and whose size equals the recorded cover value;
  5. optimal records have dual bound == cover; timeouts are kept separate
     and are only credited with their dual lower bound;
  6. reports the global minimum, the ids attaining it (with selected
     subgroup indices), the cover-value distribution, and verdicts.
"""

import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent
N = 18
N2 = N * N
NGROUPS = 176
UNIVERSE = set(range(N2))

print(f"audit root: {root}")
for name in ["covers-18.jsonl", "solutions-18.jsonl", "export-18.log"]:
    digest = hashlib.sha256((root / name).read_bytes()).hexdigest()
    print(f"SHA256 {name}: {digest}")

# ---------------------------------------------------------------- export log
log_records = {}
for raw in (root / "export-18.log").read_text(encoding="utf-8", errors="replace").splitlines():
    line = raw.strip()
    match = re.fullmatch(r"(skip|done) 324 (\d+)(?: exp (\d+)| subs (\d+) ms (\d+))", line)
    if not match:
        continue
    action, gid, exponent, subgroups, millis = match.groups()
    gid = int(gid)
    assert 1 <= gid <= NGROUPS, gid
    assert gid not in log_records, f"duplicate log entry for id {gid}"
    log_records[gid] = {
        "action": action,
        "exp": int(exponent) if exponent else None,
        "subs": int(subgroups) if subgroups else None,
        "ms": int(millis) if millis else None,
    }
assert set(log_records) == set(range(1, NGROUPS + 1)), (
    "missing ids in export log",
    sorted(set(range(1, NGROUPS + 1)) - set(log_records)),
)
skipped = {i for i, r in log_records.items() if r["action"] == "skip"}
exported = {i for i, r in log_records.items() if r["action"] == "done"}
assert skipped | exported == set(range(1, NGROUPS + 1))
assert not (skipped & exported)
for i in skipped:
    assert N % log_records[i]["exp"] != 0, i
for i in exported:
    # exported groups carry their exponent in covers-18.jsonl (checked below)
    assert log_records[i]["exp"] is None and log_records[i]["subs"] is not None
print(
    f"export log: 176/176 ids accounted, exponent-excluded={len(skipped)}, "
    f"exported={len(exported)}"
)

# ------------------------------------------------------------------- covers
covers_list = [
    json.loads(line)
    for line in (root / "covers-18.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
covers = {record["id"]: record for record in covers_list}
assert len(covers_list) == len(covers) == len(exported), (len(covers_list), len(exported))
assert set(covers) == exported
total_subgroups = 0
for gid, record in covers.items():
    assert N % record["exp"] == 0, gid
    if log_records[gid]["exp"] is not None:
        assert record["exp"] == log_records[gid]["exp"], gid
    assert len(record["subs"]) == log_records[gid]["subs"], gid
    normalized = []
    for subgroup in record["subs"]:
        assert len(subgroup) == N == len(set(subgroup)), (gid, subgroup)
        assert 0 in subgroup, gid
        assert all(type(e) is int and 0 <= e < N2 for e in subgroup), gid
        normalized.append(tuple(sorted(subgroup)))
    assert len(set(normalized)) == len(normalized), gid
    total_subgroups += len(normalized)
print(
    f"covers: {len(covers)} groups, {total_subgroups} subgroups of order 18 in total "
    f"(min {min(len(r['subs']) for r in covers.values())}, "
    f"max {max(len(r['subs']) for r in covers.values())} per group)"
)

# ---------------------------------------------------------------- solutions
solutions_list = [
    json.loads(line)
    for line in (root / "solutions-18.jsonl").read_text(encoding="utf-8").splitlines()
    if line.strip()
]
solutions = {record["id"]: record for record in solutions_list}
assert len(solutions_list) == len(solutions) == len(covers)
assert set(solutions) == set(covers)

uncoverable, optimal, timeouts = set(), set(), set()
certificates = {}
for gid, solution in solutions.items():
    cover_record = covers[gid]
    subs = cover_record["subs"]
    assert solution["variables"] == len(subs), gid
    assert solution["exp"] == cover_record["exp"], gid
    if solution.get("reason") == "uncovered elements":
        assert solution["cover"] is None and "selected" not in solution, gid
        union = set().union(*(set(s) for s in subs)) if subs else set()
        assert union != UNIVERSE, gid
        assert len(UNIVERSE - union) >= 1
        uncoverable.add(gid)
        continue
    selected = solution["selected"]
    assert len(selected) == len(set(selected)) == solution["cover"], gid
    assert all(type(j) is int and 0 <= j < solution["variables"] for j in selected), gid
    union = set().union(*(set(subs[j]) for j in selected))
    assert union == UNIVERSE, (gid, len(union))
    assert solution.get("union_size", N2) == N2, gid
    certificates[gid] = selected
    if solution["status"] == 0:
        assert solution["bound"] is not None
        assert math.isclose(solution["bound"], solution["cover"], rel_tol=0, abs_tol=1e-6), (
            gid,
            solution["bound"],
            solution["cover"],
        )
        optimal.add(gid)
    else:
        assert solution["cover"] is not None
        assert solution["bound"] is not None
        assert solution["cover"] + 1e-9 >= solution["bound"]
        timeouts.add(gid)

assert len(uncoverable) + len(optimal) + len(timeouts) == len(solutions) == len(covers)
print(
    f"solutions: noncoverable={len(uncoverable)}, optimal={len(optimal)}, "
    f"timeout={len(timeouts)}"
)

global_min = min(solutions[i]["cover"] for i in optimal)
attain = sorted(i for i in optimal if solutions[i]["cover"] == global_min)
dist = Counter(solutions[i]["cover"] for i in optimal)
timeout_info = sorted(
    (i, solutions[i]["cover"], solutions[i]["bound"], math.ceil(solutions[i]["bound"] - 1e-9))
    for i in timeouts
)

print(f"GLOBAL MINIMUM alpha(18) over covered groups = {global_min}")
print(f"  attained by {len(attain)} groups: {attain}")
print("  cover-value distribution (proved optimal only):")
for value in sorted(dist):
    ids = sorted(i for i in optimal if solutions[i]["cover"] == value)
    print(f"    {value}: {dist[value]} groups -> {ids}")

# timeouts must not be able to beat the reported minimum
for gid, cover, bound, lower in timeout_info:
    print(
        f"  TIMEOUT SmallGroup(324,{gid}): incumbent={cover}, dual bound={bound:.6f} "
        f"=> lower bound {lower}, status={solutions[gid]['status']}, "
        f"time={solutions[gid]['seconds']}s"
    )
    assert lower >= global_min, (
        f"timeout id {gid} has lower bound {lower} < global minimum {global_min}; "
        "global minimum is not resolved"
    )

# ------------------------------------------------------------- certificates
print("CERTIFICATES for the global minimum:")
for gid in attain:
    selected = certificates[gid]
    print(
        f"  CERT{global_min} SmallGroup(324,{gid}): status={solutions[gid]['status']}, "
        f"cover={solutions[gid]['cover']}, dual_bound={solutions[gid]['bound']}, "
        f"union=324/324"
    )
    print(f"    selected={selected}")

# structural sanity: every coverable group has exponent dividing 18
assert all(N % covers[i]["exp"] == 0 for i in optimal | timeouts | uncoverable)
assert all(N % log_records[i]["exp"] != 0 for i in skipped)

if global_min == 27:
    verdict = (
        "A 27-subgroup cover EXISTS; it is certified by the selected subgroups above "
        "and by the matching MILP dual bound 27 (optimality)."
    )
elif global_min >= 28:
    verdict = (
        f"No group of order 324 admits an 18-subgroup cover with 27 or fewer subgroups: "
        f"every coverable group has proved optimum >= {global_min}."
    )
else:
    verdict = f"UNEXPECTED global minimum {global_min}; inspect certificates."
assert global_min >= 27, global_min

print(verdict)
print(
    f"AUDIT RESULT: PASS; 176/176 groups accounted for "
    f"({len(skipped)} exponent-excluded, {len(uncoverable)} non-coverable, "
    f"{len(optimal)} proved optimal, {len(timeouts)} time-limited with dual bounds); "
    "every saved selected cover was re-expanded and checked to cover 324/324."
)
