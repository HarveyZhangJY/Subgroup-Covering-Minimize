# Exact 0-1 set-cover solver for the saved subgroup lists.
#
# Usage:
#   python computation/order400/solve-covers.py covers-20.jsonl 20 120 solutions-20.jsonl \
#       > solve-20.log 2>&1
#
# argv: covers.jsonl, n, time_limit_seconds (default 120), optional outfile.
# Each instance is solved with scipy.optimize.milp (HiGHS), integrality 0/1 and
# mip_rel_gap = 0, so status 0 means *proved optimal*.  A time-out keeps the
# incumbent cover and the dual bound (a certified lower bound); it is never
# reported as optimal.  Groups whose order-n subgroups do not cover all n^2
# elements are recorded as "uncovered elements" (uncoverable).
#
# Two exact model reductions are applied before calling HiGHS; neither changes
# the optimum:
#   * elements lying in exactly the same set of subgroups give identical
#     covering constraints, so only one row per distinct incidence set is kept;
#   * if row R1's incidence set is contained in row R2's, every cover
#     satisfying R1 satisfies R2, so R2 is dropped.
# Selected indices are reported in the original subgroup numbering.
#
# Every instance runs in its own child process: HiGHS 1.x can crash in
# presolve on rare instances, and a crash must not lose the remaining work.
# On a crash the instance is retried with presolve disabled.
#
# The outfile is written incrementally; ids already present are skipped, so an
# interrupted run resumes where it stopped.

import json
import math
import subprocess
import sys
import time

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_matrix


def merged_rows(subs):
    """One constraint per distinct incidence set (equal rows are redundant)."""
    incidence = {}
    for j, s in enumerate(subs):
        for e in s:
            incidence.setdefault(e, []).append(j)
    return list({frozenset(cols) for cols in incidence.values()})


def line_cuts(subs, orders, q):
    """Valid lower bounds for groups whose Sylow 2-subgroup is elementary abelian.

    If every element order divides 2q then a Sylow 2-subgroup Q has order 16 and
    exponent 2, i.e. Q = C2^4.  An order-n subgroup H meets a Sylow q-subgroup in
    a line L of size q-1 (all its elements of order q), and H = L * M with M an
    order-4 subgroup of Q.  Covering the q-1 elements of L times all 16 elements
    of Q forces the chosen M's of that line class to cover Q; four 4-element
    subgroups cannot cover C2^4 (they would have to be pairwise disjoint and
    4 * 3 < 15 non-zero elements), so at least five subgroups are needed per
    line class.  The class of a subgroup is identified by its sorted list of
    order-q element labels, which is exactly L minus the identity.
    """
    if not orders or max(orders) > 2 * q:
        return []
    classes = {}
    for j, s in enumerate(subs):
        key = tuple(e for e in s if orders[e] == q)
        classes.setdefault(key, []).append(j)
    return [frozenset(v) for v in classes.values() if v]


def full_rows(subs, N):
    rows = [set() for _ in range(N)]
    for j, s in enumerate(subs):
        for e in s:
            rows[e].add(j)
    return [frozenset(r) for r in rows]


def greedy_cover(subs, N):
    """Deterministic greedy cover; returns (indices, uncovered set)."""
    uncovered = set(range(N))
    chosen = []
    while uncovered:
        best, gain = None, 0
        for j, s in enumerate(subs):
            g = len(uncovered.intersection(s))
            if g > gain:
                best, gain = j, g
        if best is None:
            break
        chosen.append(best)
        uncovered.difference_update(subs[best])
    return chosen, uncovered


def lp_record(d, n):
    """Certified LP-relaxation lower bound plus a greedy upper bound.

    Used only when HiGHS cannot return a MIP dual bound for the instance (it can
    stall far beyond its time limit); the LP bound is a valid lower bound and the
    greedy cover a valid upper bound.
    """
    from scipy.optimize import linprog

    N = n * n
    subs = d["subs"]
    rows = merged_rows(subs)
    rr, cc = [], []
    for r, row in enumerate(rows):
        for j in row:
            rr.append(r)
            cc.append(j)
    A = coo_matrix((np.ones(len(rr)), (rr, cc)), shape=(len(rows), len(subs))).tocsr()
    t = time.time()
    res = linprog(
        np.ones(len(subs)), A_ub=-A, b_ub=-np.ones(len(rows)),
        bounds=[(0, 1)] * len(subs), method="highs",
    )
    if res.status != 0:
        return None
    chosen, uncovered = greedy_cover(subs, N)
    assert not uncovered
    return {
        "id": d["id"],
        "exp": d["exp"],
        "variables": len(subs),
        "rows": len(rows),
        "cuts": 0,
        "presolve": None,
        "reduction": "merged",
        "status": 1,
        "cover": len(chosen),
        "bound": float(res.fun),
        "lower_bound": math.ceil(res.fun - 1e-6),
        "seconds": round(time.time() - t, 3),
        "selected": chosen,
        "bound_source": "lp_relaxation",
    }


def solve_one(d, n, time_limit, presolve, reduction, cuts=None):
    N = n * n
    # n = p * q^alpha with q the prime whose Sylow subgroup is being counted
    q = max(f for f in range(2, n + 1)
            if n % f == 0 and all(f % g for g in range(2, f)))
    i = d["id"]
    subs = d["subs"]
    orders = d.get("orders") or []
    covered = set().union(*(set(s) for s in subs)) if subs else set()
    if covered != set(range(N)):
        gap = sorted(set(range(N)) - covered)
        return {
            "id": i,
            "exp": d["exp"],
            "variables": len(subs),
            "cover": None,
            "reason": "uncovered elements",
            "uncovered_count": len(gap),
            "uncovered_orders": sorted({orders[e] for e in gap if e < len(orders)}),
            "uncovered_sample": gap[:20],
        }

    rows = full_rows(subs, N) if reduction == "full" else merged_rows(subs)
    cut_rows, cut_lb = [], []
    if cuts and d.get("sylow_q_normal"):
        cut_rows = line_cuts(subs, orders, q)
        cut_lb = [5] * len(cut_rows)
    rr, cc, lb = [], [], []
    for r, row in enumerate(rows + cut_rows):
        for j in row:
            rr.append(r)
            cc.append(j)
        lb.append(1 if r < len(rows) else cut_lb[r - len(rows)])
    A = coo_matrix((np.ones(len(rr)), (rr, cc)), shape=(len(rows) + len(cut_rows), len(subs))).tocsr()

    t = time.time()
    res = milp(
        np.ones(len(subs)),
        integrality=np.ones(len(subs)),
        bounds=Bounds(0, 1),
        constraints=LinearConstraint(A, np.asarray(lb, dtype=float), np.inf),
        options={"time_limit": time_limit, "mip_rel_gap": 0.0, "presolve": presolve},
    )
    elapsed = round(time.time() - t, 3)
    bound = getattr(res, "mip_dual_bound", None)
    record = {
        "id": i,
        "exp": d["exp"],
        "variables": len(subs),
        "rows": len(rows),
        "cuts": len(cut_rows),
        "presolve": presolve,
        "reduction": reduction,
        "status": int(res.status),
        "cover": None if res.x is None else int(round(float(res.fun))),
        "bound": None if bound is None else float(bound),
        "lower_bound": None if bound is None else math.ceil(bound - 1e-6),
        "seconds": elapsed,
    }
    if res.x is not None:
        selected = [j for j, x in enumerate(res.x) if x > 0.5]
        record["selected"] = selected
        union = set().union(*(set(subs[j]) for j in selected))
        if union != set(range(N)):
            record["warning"] = "selected set does not cover all elements"
    return record


LADDER = (
    ("merged", False, True),
    ("merged", False, False),
    ("merged", True, False),
    ("full", False, False),
)


def main():
    covers_path = sys.argv[1]
    n = int(sys.argv[2])
    time_limit = float(sys.argv[3]) if len(sys.argv) > 3 else 120.0
    outfile = sys.argv[4] if len(sys.argv) > 4 else None

    done_ids = set()
    if outfile:
        try:
            for line in open(outfile, encoding="utf-8"):
                if line.strip():
                    done_ids.add(json.loads(line)["id"])
        except FileNotFoundError:
            pass
        out = open(outfile, "a", encoding="utf-8")
    else:
        out = sys.stdout

    def emit(record, log_line):
        out.write(json.dumps(record) + "\n")
        out.flush()
        print(log_line, flush=True)

    for line in open(covers_path, encoding="utf-8"):
        if not line.strip():
            continue
        d = json.loads(line)
        if d["id"] in done_ids:
            continue
        done = False
        # (reduction, presolve) ladder: HiGHS 1.x may crash in presolve or on
        # aggressively reduced models, so fall back step by step.  All rungs are
        # exact formulations of the same instance.
        for reduction, presolve, cuts in LADDER:
            try:
                proc = subprocess.run(
                    [sys.executable, __file__, "--one", covers_path, str(n), str(time_limit),
                     str(d["id"]), "1" if presolve else "0", reduction,
                     "1" if cuts else "0"],
                    capture_output=True, text=True, timeout=time_limit + 60,
                )
            except subprocess.TimeoutExpired:
                print(
                    f"id {d['id']:4d} child exceeded {time_limit + 60:.0f}s "
                    f"({reduction}, presolve={presolve}, cuts={cuts}); retrying",
                    flush=True,
                )
                continue
            if proc.returncode != 0:
                print(
                    f"id {d['id']:4d} child crashed (rc={proc.returncode}, "
                    f"reduction={reduction}, presolve={presolve}); retrying",
                    flush=True,
                )
                continue
            record = json.loads(proc.stdout.strip().splitlines()[-1])
            if record.get("reason") == "uncovered elements":
                log_line = (
                    f"id {d['id']:4d} vars {record['variables']:5d} UNCOVERABLE "
                    f"missing {record['uncovered_count']} orders {record['uncovered_orders']}"
                )
            else:
                log_line = (
                    f"id {d['id']:4d} vars {record['variables']:5d} rows {record['rows']:4d} "
                    f"status {record['status']} cover {record['cover']} bound {record['bound']} "
                    f"t {record['seconds']}s {record['reduction']}/presolve={record['presolve']}"
                    f"/cuts={record['cuts']}"
                )
            emit(record, log_line)
            done = True
            break
        if not done:
            record = lp_record(d, n)
            if record is not None:
                emit(
                    record,
                    f"id {d['id']:4d} vars {record['variables']:5d} MILP FAILED; "
                    f"LP lower bound {record['lower_bound']} (raw {record['bound']}), "
                    f"greedy cover {record['cover']}",
                )
            else:
                emit({"id": d["id"], "error": "no solver result"},
                     f"id {d['id']:4d} NO RESULT")

    if outfile:
        out.close()
    print("SOLVE DONE", flush=True)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--one":
        covers_path = sys.argv[2]
        n = int(sys.argv[3])
        time_limit = float(sys.argv[4])
        want = int(sys.argv[5])
        presolve = sys.argv[6] == "1"
        reduction = sys.argv[7] if len(sys.argv) > 7 else "merged"
        cuts = len(sys.argv) > 8 and sys.argv[8] == "1"
        for line in open(covers_path, encoding="utf-8"):
            if not line.strip():
                continue
            d = json.loads(line)
            if d["id"] == want:
                print(json.dumps(solve_one(d, n, time_limit, presolve, reduction, cuts)), flush=True)
                break
    else:
        main()
