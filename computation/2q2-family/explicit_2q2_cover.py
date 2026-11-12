#!/usr/bin/env python3
"""Explicit 3*ell^2 cover of G = F_ell^4 : C_2^2 for odd primes ell.

Group action (faithful, no kernel):
  a = diag(-1,-1, 1,-1),   b = diag( 1, 1,-1,-1)
on Q = F_ell^4 with basis e0,e1,e2,e3.

For n = 2*ell^2 the group order is n^2 and the cover has
3*ell^2 = n + ell^2 subgroups of order n, meeting the normal-Sylow
lower bound.  The combinatorial input is explicit: an irreducible
quadratic polynomial gives an affine line spread of AG(3,ell) with
directions outside a fixed plane.
"""

import itertools
import sys
import time

# ---------- finite field helpers ----------

def is_square(x, ell):
    x %= ell
    if x == 0:
        return True
    return any((a * a) % ell == x for a in range(1, ell))


def irreducible_companion(ell):
    """Return C = [[0,-q],[1,0]] with x^2+q irreducible over F_ell."""
    for q in range(1, ell):
        if not is_square((-q) % ell, ell):
            return q
    raise RuntimeError


def spread_lines(ell):
    """Return the explicit spread: list of (direction_ab, offset_fg, points)."""
    q = irreducible_companion(ell)
    # C = [[0, -q], [1, 0]]
    def C(a, b):
        return ((-q * b) % ell, a % ell)
    lines = []
    for a in range(ell):
        for b in range(ell):
            f, g = C(a, b)
            pts = frozenset(((a * t + f) % ell,
                             (b * t + g) % ell,
                             t % ell) for t in range(ell))
            lines.append(((a, b), (f, g), pts))
    # verify partition of V = F_ell^3
    union = set()
    for _, _, pts in lines:
        assert len(pts) == ell
        assert not (union & pts)
        union |= pts
    assert union == set(itertools.product(range(ell), repeat=3))
    return lines


# ---------- group and cover ----------

class Cover:
    def __init__(self, ell):
        self.ell = ell
        self.n = 2 * ell * ell
        self.Q = list(itertools.product(range(ell), repeat=4))
        self.qindex = {q: i for i, q in enumerate(self.Q)}
        self.subs = []       # list of frozensets of element ids
        self.meta = []

    def vadd(self, a, b):
        ell = self.ell
        return tuple((x + y) % ell for x, y in zip(a, b))

    def vscale(self, c, a):
        ell = self.ell
        return tuple((c * x) % ell for x in a)

    def act(self, s, q):
        ell = self.ell
        signs = {
            0: (1, 1, 1, 1),
            1: (ell - 1, ell - 1, 1, ell - 1),
            2: (1, 1, ell - 1, ell - 1),
            3: (ell - 1, ell - 1, ell - 1, 1),
        }[s]
        return tuple((signs[i] * q[i]) % ell for i in range(4))

    def gid(self, q, s):
        return self.qindex[q] * 4 + s

    def span2(self, v, w):
        ell = self.ell
        out = set()
        for c1 in range(ell):
            for c2 in range(ell):
                out.add(self.vadd(self.vscale(c1, v), self.vscale(c2, w)))
        return out

    def add(self, M, u, k, tag):
        assert self.vadd(u, self.act(k, u)) in M, (tag, u, k)
        for m in M:
            assert self.act(k, m) in M, (tag, 'M not invariant')
        H = set()
        for m in M:
            H.add(self.gid(m, 0))
            H.add(self.gid(self.vadd(u, m), k))
        assert len(H) == self.n
        self.subs.append(frozenset(H))
        self.meta.append({'k': k, 'M': sorted(M), 'u': u, 'tag': tag})

    def build(self):
        ell = self.ell
        e0 = (1, 0, 0, 0)
        e1 = (0, 1, 0, 0)
        e2 = (0, 0, 1, 0)
        e3 = (0, 0, 0, 1)
        def line(v):
            return set(self.vscale(c, v) for c in range(ell))
        L2 = line(e2)
        L3 = line(e3)
        P = self.span2(e0, e1)
        lines = spread_lines(ell)
        # K = <a>: Q/L2 coordinates (e0,e1,e3); lift direction (a,b,1)
        for (a, b), (f, g), _ in lines:
            w = self.vadd(self.vadd(self.vscale(a, e0), self.vscale(b, e1)), e3)
            u = self.vadd(self.vscale(f, e0), self.vscale(g, e1))
            M = self.span2(e2, w)
            assert len(M) == ell * ell
            self.add(M, u, 1, 'a')
        # K = <ab>: Q/L3 coordinates (e0,e1,e2); lift direction (a,b,1)
        for (a, b), (f, g), _ in lines:
            w = self.vadd(self.vadd(self.vscale(a, e0), self.vscale(b, e1)), e2)
            u = self.vadd(self.vscale(f, e0), self.vscale(g, e1))
            M = self.span2(e3, w)
            assert len(M) == ell * ell
            self.add(M, u, 3, 'ab')
        # K = <b>: all cosets of P
        for x in range(ell):
            for y in range(ell):
                u = self.vadd(self.vscale(x, e2), self.vscale(y, e3))
                self.add(P, u, 2, 'b')

    def verify(self, full_pair_check=False):
        ell = self.ell
        n = self.n
        N = 4 * ell ** 4
        assert len(self.subs) == 3 * ell * ell
        assert len(set(self.subs)) == len(self.subs)
        # algebraic subgroup check is done in add(); optionally pair-check
        if full_pair_check:
            def mul(g, h):
                q, s = divmod(g, 4)
                r, t = divmod(h, 4)
                q = self.Q[q]
                r = self.Q[r]
                signs = {
                    0: (1, 1, 1, 1),
                    1: (ell - 1, ell - 1, 1, ell - 1),
                    2: (1, 1, ell - 1, ell - 1),
                    3: (ell - 1, ell - 1, ell - 1, 1),
                }[s]
                qq = tuple((q[i] + signs[i] * r[i]) % ell for i in range(4))
                return self.qindex[qq] * 4 + (s ^ t)
            for H in self.subs:
                Hs = set(H)
                for g in H:
                    for h in H:
                        assert mul(g, h) in Hs
        union = set().union(*self.subs)
        assert union == set(range(N)), (len(union), N)
        # identity fiber covered by kernels
        kernels = set()
        for m in self.meta:
            kernels |= set(m['M'])
        assert kernels == set(self.Q)
        # each nonidentity fiber partitioned
        for k in (1, 2, 3):
            fiber = set(range(k, N, 4))
            blocks = [set(H) & fiber for H, m in zip(self.subs, self.meta)
                      if m['k'] == k]
            assert sum(len(b) for b in blocks) == len(fiber)
            assert set().union(*blocks) == fiber
        return True


def run(ell, pair_check=False):
    t0 = time.time()
    C = Cover(ell)
    C.build()
    C.verify(full_pair_check=pair_check)
    print(f"ell={ell:2d}: n={C.n:4d}, |G|={4*ell**4:7d}, "
          f"subgroups={len(C.subs):4d} (=3*ell^2), cover OK, "
          f"time={time.time()-t0:.2f}s")


if __name__ == '__main__':
    ells = [int(x) for x in sys.argv[1:]] or [3, 5, 7, 11, 13]
    for ell in ells:
        run(ell, pair_check=(ell == 3))
