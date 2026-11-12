#!/usr/bin/env python3
"""Search a non-normal-Sylow-3 group of order 324 for small 18-subgroup covers.

Group: G = V : P with V = C_2^2, P = C_3^4.
A linear functional phi: P -> F_3 (first coordinate) makes P act on V
through an order-3 automorphism T of V.  Then V is normal, P is not normal,
and n_3(G) = 4.  The group has exponent 6, so every order-18 subgroup has
a 2-part equal to one of the three involutions of V.

We enumerate all subgroups of order 18 and solve the exact set-cover MILP.
"""

import itertools
import json
import time

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix

# ---------- P = F_3^4 ----------
P = list(itertools.product(range(3), repeat=4))
pindex = {p: i for i, p in enumerate(P)}
PZERO = (0, 0, 0, 0)


def padd(a, b):
    return tuple((x + y) % 3 for x, y in zip(a, b))


def pneg(a):
    return tuple((-x) % 3 for x in a)


# ---------- V = C_2^2 as 2-bit vectors ----------
# 0=00, 1=10, 2=01, 3=11.  T(a,b)=(b,a+b).
def T(v):
    a = (v >> 0) & 1
    b = (v >> 1) & 1
    return ((b) | ((a ^ b) << 1)) & 3


def Tpow(v, k):
    for _ in range(k % 3):
        v = T(v)
    return v


def phi(p):
    return p[0]


# group element (v,p) -> v*81 + pindex[p]
def gid(v, p):
    return v * 81 + pindex[p]


def gunpack(g):
    return divmod(g, 81)


def gmul(g, h):
    v, pi = gunpack(g)
    w, qi = gunpack(h)
    p = P[pi]
    q = P[qi]
    vv = v ^ Tpow(w, phi(p))
    return gid(vv, padd(p, q))


def ginv(g):
    v, pi = gunpack(g)
    p = P[pi]
    k = phi(p)
    return gid(Tpow(v, (-k) % 3), pneg(p))


def element_order(g):
    e = 0
    x = g
    o = 1
    while x != e:
        x = gmul(x, g)
        o += 1
        assert o <= 324
    return o


# ---------- all 2-dim subspaces of P ----------
def all_2d_subspaces():
    subs = set()
    for a in P:
        if a == PZERO:
            continue
        for b in P:
            if b == PZERO or b == a or b == pneg(a):
                continue
            span = set()
            for c1 in range(3):
                for c2 in range(3):
                    span.add(padd(tuple(c1 * x % 3 for x in a),
                                  tuple(c2 * x % 3 for x in b)))
            subs.add(frozenset(span))
    return [sorted(s) for s in subs]


SUBSPACES = all_2d_subspaces()
print("2-dim subspaces of C_3^4:", len(SUBSPACES))


# ---------- enumerate order-18 subgroups ----------
def closure(gens):
    K = {0}
    K.update(gens)
    changed = True
    while changed:
        changed = False
        for x in list(K):
            for y in list(K):
                z = gmul(x, y)
                if z not in K:
                    K.add(z)
                    changed = True
    return K


def enumerate_subgroups():
    seen = set()
    out = []
    for Q in SUBSPACES:
        q1 = next(x for x in Q if x != PZERO)
        q2 = next(x for x in Q if x != PZERO and
                  x != q1 and x != pneg(q1))
        for v1 in range(4):
            for v2 in range(4):
                g1 = gid(v1, q1)
                g2 = gid(v2, q2)
                K = closure([g1, g2])
                if len(K) != 18:
                    continue
                # check it is really a subgroup of order 18 and record
                Kf = frozenset(K)
                if Kf not in seen:
                    seen.add(Kf)
                    out.append(Kf)
    return out


def solve_cover(subs, time_limit=180):
    n = len(subs)
    A = lil_matrix((324, n), dtype=float)
    for j, H in enumerate(subs):
        for e in H:
            A[e, j] = 1
    res = milp(np.ones(n), integrality=np.ones(n), bounds=Bounds(0, 1),
               constraints=LinearConstraint(A.tocsr(), 1, np.inf),
               options={'time_limit': time_limit, 'mip_rel_gap': 0, 'presolve': True})
    sel = None if res.x is None else [j for j, x in enumerate(res.x) if x > .5]
    return {
        'status': int(res.status),
        'objective': None if res.fun is None else round(float(res.fun), 9),
        'dual_bound': None if getattr(res, 'mip_dual_bound', None) is None else float(res.mip_dual_bound),
        'variables': n,
        'selected': sel,
    }


def main():
    t0 = time.time()
    groups = enumerate_subgroups()
    union = set().union(*groups) if groups else set()
    print(f"order-18 subgroups: {len(groups)} (enumeration {time.time()-t0:.2f}s)")
    print(f"union of all order-18 subgroups: {len(union)}/324; "
          f"missing {324-len(union)}; coverable={len(union)==324}")
    res = solve_cover(groups)
    print(res)
    if res['selected'] is not None:
        selected_union = set().union(*(set(groups[j]) for j in res['selected']))
        print("selected union:", len(selected_union), "/324")
    # exponent check
    orders = {}
    for g in range(324):
        o = element_order(g)
        orders[o] = orders.get(o, 0) + 1
    print("element orders:", dict(sorted(orders.items())))
    with open('n18_nonnormal_results.json', 'w', encoding='utf-8') as f:
        json.dump({'subgroups': len(groups),
                   'union_size': len(union),
                   'uncoverable': len(union) != 324,
                   'milp': {k: v for k, v in res.items() if k != 'selected'},
                   'selected_sets': None if res['selected'] is None else
                   [sorted(groups[j]) for j in res['selected']]}, f, indent=1)


if __name__ == '__main__':
    main()
