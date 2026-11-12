#!/usr/bin/env python3
"""Exact cover search for groups G = F_3^4 : C_2^2 of order 324.

All C_2^2-actions on F_3^4 are diagonalizable over F_3, so the actions are
classified by the multiset of characters on the four coordinate axes.
For each faithful action we enumerate every subgroup of order 18 and solve
the exact set-cover MILP for the minimum number of order-18 subgroups.
"""

import itertools
import json
import sys
import time

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix

# ---------- F_3^4 and A = C_2^2 ----------

ZERO = (0, 0, 0, 0)
Q = list(itertools.product(range(3), repeat=4))
qindex = {v: i for i, v in enumerate(Q)}


def vadd(v, w):
    return ((v[0] + w[0]) % 3, (v[1] + w[1]) % 3,
            (v[2] + w[2]) % 3, (v[3] + w[3]) % 3)


def vneg(v):
    return ((-v[0]) % 3, (-v[1]) % 3, (-v[2]) % 3, (-v[3]) % 3)


def vscale(c, v):
    return ((c * v[0]) % 3, (c * v[1]) % 3,
            (c * v[2]) % 3, (c * v[3]) % 3)


def is_zero(v):
    return v == ZERO


def independent(v, w):
    # over F_3, two nonzero vectors are dependent iff one is +- the other
    if is_zero(v) or is_zero(w):
        return False
    return v != w and v != vneg(w)


# action of A element a on a coordinate with character char=(sa,sb)
# A elements: 0, a=1, b=2, ab=3 (XOR)
def sign_of(char, a):
    sa, sb = char
    e = (sa * (a & 1) + sb * ((a >> 1) & 1)) % 2
    return 1 if e == 0 else 2  # 2 == -1 mod 3


def act(chars, a, v):
    return tuple((sign_of(chars[i], a) * v[i]) % 3 for i in range(4))


# ---------- all 2-dimensional subspaces of F_3^4 ----------

def all_2d_subspaces():
    subs = set()
    for v in Q:
        if is_zero(v):
            continue
        for w in Q:
            if not independent(v, w):
                continue
            span = set()
            for c1 in range(3):
                for c2 in range(3):
                    span.add(vadd(vscale(c1, v), vscale(c2, w)))
            subs.add(frozenset(span))
    return sorted((sorted(s) for s in subs), key=lambda M: tuple(M))


SUBSPACES_2D = all_2d_subspaces()


def invariant_subspaces(chars, k):
    out = []
    for M in SUBSPACES_2D:
        if all(act(chars, k, m) in set(M) for m in M):
            out.append(M)
    return out


# ---------- group G = Q : A ----------

def gid(v, a):
    return qindex[v] * 4 + a


def enumerate_subgroups(chars):
    """Return list of frozensets of element ids, one per distinct order-18 subgroup."""
    seen = set()
    subgroups = []
    meta = []
    for k in (1, 2, 3):
        for M in invariant_subspaces(chars, k):
            Mset = set(M)
            local = set()
            for u in Q:
                off = vadd(u, vneg(act(chars, k, u)))  # u - D_k u
                H = set()
                for m in M:
                    H.add(gid(m, 0))
                    H.add(gid(vadd(off, m), k))
                if len(H) != 18:
                    continue
                Hf = frozenset(H)
                if Hf not in local:
                    local.add(Hf)
            for Hf in sorted(local, key=lambda H: tuple(sorted(H))):
                if Hf not in seen:
                    seen.add(Hf)
                    subgroups.append(Hf)
                    meta.append({'k': k, 'M': [list(m) for m in M]})
    return subgroups, meta


def solve_cover(subgroups, element_count=324, time_limit=120, upper=None):
    n = len(subgroups)
    A = lil_matrix((element_count, n), dtype=float)
    for j, H in enumerate(subgroups):
        for e in H:
            A[e, j] = 1
    A = A.tocsr()
    constraints = [LinearConstraint(A, 1, np.inf)]
    if upper is not None:
        row = lil_matrix((1, n), dtype=float)
        for j in range(n):
            row[0, j] = 1
        constraints.append(LinearConstraint(row.tocsr(), -np.inf, upper))
    t0 = time.time()
    res = milp(np.ones(n), integrality=np.ones(n),
               bounds=Bounds(0, 1), constraints=constraints,
               options={'time_limit': time_limit, 'mip_rel_gap': 0, 'presolve': True})
    dt = time.time() - t0
    selected = None
    if res.x is not None:
        selected = [j for j, x in enumerate(res.x) if x > 0.5]
    return {
        'status': int(res.status),
        'objective': None if res.fun is None else round(float(res.fun), 9),
        'dual_bound': None if getattr(res, 'mip_dual_bound', None) is None else float(res.mip_dual_bound),
        'selected': selected,
        'variables': n,
        'seconds': round(dt, 3),
    }


def verify(subgroups, selected):
    union = set()
    for j in selected:
        union |= set(subgroups[j])
    return len(union) == 324


# ---------- character assignments ----------

def faithful(chars):
    # characters must span the dual of C_2^2: at least two independent
    # nonzero characters among the four coordinates
    nonzero = {c for c in chars if c != (0, 0)}
    if len(nonzero) < 2:
        return False
    cs = list(nonzero)
    # over F_2, any two distinct nonzero vectors are independent
    return len(cs) >= 2


def canonical(chars):
    # quotient by permutations of the three nonzero characters (GL(2,2))
    # and by coordinate permutations (multiset)
    perms = [
        {0: 0, 1: 1, 2: 2, 3: 3},
        {0: 0, 1: 2, 2: 1, 3: 3},
        {0: 0, 1: 3, 2: 2, 3: 1},
        {0: 0, 1: 1, 2: 3, 3: 2},
        {0: 0, 1: 2, 2: 3, 3: 1},
        {0: 0, 1: 3, 2: 1, 3: 2},
    ]
    # encode character (sa,sb) as integer sa+2*sb: 0,1,2,3
    enc = [c[0] + 2 * c[1] for c in chars]
    best = None
    for p in perms:
        t = tuple(sorted(p[x] for x in enc))
        if best is None or t < best:
            best = t
    return best


def decode_enc(e):
    return (e % 2, e // 2)


def all_actions():
    reps = {}
    for chars in itertools.product([(0, 0), (1, 0), (0, 1), (1, 1)], repeat=4):
        if not faithful(chars):
            continue
        key = canonical(chars)
        if key not in reps:
            reps[key] = chars
    return reps


def main():
    reps = all_actions()
    print(f"distinct faithful actions: {len(reps)}", flush=True)
    results = {}
    for key, chars in sorted(reps.items()):
        label = ''.join(str(x) for x in key)
        print(f"\n=== action {label} chars={chars} ===", flush=True)
        t0 = time.time()
        subs, meta = enumerate_subgroups(chars)
        print(f"  order-18 subgroups: {len(subs)} (enumeration {time.time()-t0:.2f}s)", flush=True)
        res = solve_cover(subs, time_limit=180)
        print(f"  MILP: {res}", flush=True)
        if res['selected'] is not None:
            ok = verify(subs, res['selected'])
            print(f"  union check: {ok}", flush=True)
        results[label] = {
            'chars': chars,
            'subgroups': len(subs),
            'milp': {k: v for k, v in res.items() if k != 'selected'},
            'selected': res['selected'],
            'selected_sets': None if res['selected'] is None else [sorted(subs[j]) for j in res['selected']],
            'selected_meta': None if res['selected'] is None else [meta[j] for j in res['selected']],
        }
        with open('n18_results.json', 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
