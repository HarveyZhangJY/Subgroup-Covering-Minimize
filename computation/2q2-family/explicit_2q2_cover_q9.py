#!/usr/bin/env python3
"""Verify the 3*q^2 cover for q=9 (n=162) over F_9.

Field: F_9 = F_3[i]/(i^2+1), elements encoded as (a,b) = a + b i.
Group: Q = F_9^4, A = C_2^2 with the faithful action
  a = diag(-1,-1,1,-1), b = diag(1,1,-1,-1).
Cover: 3*9^2 = 243 subgroups of order 162, built from the explicit
affine spread of AG(3,9) given by an irreducible quadratic over F_9.
"""

import itertools
import time

# ---------- F_9 arithmetic ----------
# elements (a,b), a,b in {0,1,2}; i^2 = -1 = 2.
F9 = [(a, b) for a in range(3) for b in range(3)]
F9ZERO = (0, 0)
F9ONE = (1, 0)


def fadd(x, y):
    return ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)


def fneg(x):
    return ((-x[0]) % 3, (-x[1]) % 3)


def fsub(x, y):
    return fadd(x, fneg(y))


def fmul(x, y):
    a, b = x
    c, d = y
    # (a+bi)(c+di) = ac - bd + (ad+bc)i
    return ((a * c - b * d) % 3, (a * d + b * c) % 3)


def fpow(x, k):
    r = F9ONE
    while k:
        if k & 1:
            r = fmul(r, x)
        x = fmul(x, x)
        k >>= 1
    return r


def finv(x):
    assert x != F9ZERO
    return fpow(x, 7)  # F_9^* has order 8


def find_nonsquare():
    squares = {fmul(x, x) for x in F9 if x != F9ZERO}
    for x in F9:
        if x != F9ZERO and x not in squares:
            return x
    raise RuntimeError


NONSQUARE = find_nonsquare()
print("non-square theta for x^2 - theta:", NONSQUARE)

# ---------- Q = F_9^4, A = C_2^2 ----------

Q = list(itertools.product(F9, repeat=4))
qindex = {q: i for i, q in enumerate(Q)}
E = [(F9ONE, F9ZERO, F9ZERO, F9ZERO),
     (F9ZERO, F9ONE, F9ZERO, F9ZERO),
     (F9ZERO, F9ZERO, F9ONE, F9ZERO),
     (F9ZERO, F9ZERO, F9ZERO, F9ONE)]


def vaddx(x, y):
    return tuple(fadd(a, b) for a, b in zip(x, y))


def vnegx(x):
    return tuple(fneg(a) for a in x)


def vscalex(c, x):
    return tuple(fmul(c, a) for a in x)


def vzero():
    return tuple(F9ZERO for _ in range(4))


def act(s, q):
    minus = (2, 0)  # -1 in F_9
    signs = {
        0: (1, 1, 1, 1),
        1: (minus, minus, (1, 0), minus),
        2: ((1, 0), (1, 0), minus, minus),
        3: (minus, minus, minus, (1, 0)),
    }[s]
    return tuple(fmul(signs[i], q[i]) for i in range(4))


def gid(q, s):
    return qindex[q] * 4 + s


def span2(v, w):
    out = set()
    for c1 in F9:
        for c2 in F9:
            out.add(vaddx(vscalex(c1, v), vscalex(c2, w)))
    return out


def line(v):
    return set(vscalex(c, v) for c in F9)


# ---------- explicit spread of AG(3,9) ----------
# C = [[0, theta],[1,0]] for x^2 - theta; theta nonsquare => tI+C invertible.
THETA = NONSQUARE


def Cmap(u, v):
    return (fmul(THETA, v), u)


def spread_lines():
    lines = []
    for u in F9:
        for v in F9:
            f, g = Cmap(u, v)
            pts = frozenset((fadd(fmul(u, t), f), fadd(fmul(v, t), g), t)
                            for t in F9)
            lines.append(((u, v), (f, g), pts))
    union = set()
    for _, _, pts in lines:
        assert len(pts) == 9 and not (union & pts)
        union |= pts
    assert union == set(itertools.product(F9, repeat=3))
    return lines


# ---------- cover ----------
subs = []
metas = []


def add_subgroup(M, u, k, tag):
    assert vaddx(u, act(k, u)) in M, (tag, u, k)
    for m in M:
        assert act(k, m) in M
    H = set()
    for m in M:
        H.add(gid(m, 0))
        H.add(gid(vaddx(u, m), k))
    assert len(H) == 162
    subs.append(frozenset(H))
    metas.append({'k': k, 'M': sorted(M), 'u': u, 'tag': tag})


def build():
    e0, e1, e2, e3 = E
    L2 = line(e2)
    L3 = line(e3)
    P = span2(e0, e1)
    lines = spread_lines()
    # K=<a>
    for (u, v), (f, g), _ in lines:
        w = vaddx(vaddx(vscalex(u, e0), vscalex(v, e1)), e3)
        x = vaddx(vscalex(f, e0), vscalex(g, e1))
        M = span2(e2, w)
        assert len(M) == 81
        add_subgroup(M, x, 1, 'a')
    # K=<ab>
    for (u, v), (f, g), _ in lines:
        w = vaddx(vaddx(vscalex(u, e0), vscalex(v, e1)), e2)
        x = vaddx(vscalex(f, e0), vscalex(g, e1))
        M = span2(e3, w)
        assert len(M) == 81
        add_subgroup(M, x, 3, 'ab')
    # K=<b>
    for r in F9:
        for s in F9:
            y = vaddx(vscalex(r, e2), vscalex(s, e3))
            add_subgroup(P, y, 2, 'b')


def verify():
    N = 4 * 9 ** 4
    assert len(subs) == 243
    assert len(set(subs)) == 243
    union = set().union(*subs)
    assert union == set(range(N)), (len(union), N)
    kernels = set()
    for m in metas:
        kernels |= set(m['M'])
    assert kernels == set(Q)
    for k in (1, 2, 3):
        fiber = set(range(k, N, 4))
        blocks = [set(H) & fiber for H, m in zip(subs, metas) if m['k'] == k]
        assert sum(len(b) for b in blocks) == len(fiber)
        assert set().union(*blocks) == fiber
    print(f"q=9: n=162, |G|={N}, subgroups={len(subs)} (=3*9^2), cover OK")


if __name__ == '__main__':
    t0 = time.time()
    build()
    verify()
    print(f"time={time.time()-t0:.2f}s")
