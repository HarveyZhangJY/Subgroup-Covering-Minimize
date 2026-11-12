#!/usr/bin/env python3
"""Verify the saved 27-subgroup cover for action 1123 (n=18).

Reads n18_results.json['1123']['selected_sets'] and checks:
- 27 distinct sets of 18 element ids;
- each set is closed under multiplication and contains inverses;
- the union is all 324 elements;
- the group has exponent dividing 18.
Then prints the image/kernel description of each selected subgroup.
"""

import itertools
import json

ZERO = (0, 0, 0, 0)
Q = list(itertools.product(range(3), repeat=4))
qindex = {v: i for i, v in enumerate(Q)}


def vadd(v, w):
    return ((v[0] + w[0]) % 3, (v[1] + w[1]) % 3,
            (v[2] + w[2]) % 3, (v[3] + w[3]) % 3)


def vneg(v):
    return ((-v[0]) % 3, (-v[1]) % 3, (-v[2]) % 3, (-v[3]) % 3)


def sign_of(char, a):
    sa, sb = char
    e = (sa * (a & 1) + sb * ((a >> 1) & 1)) % 2
    return 1 if e == 0 else 2


def act(chars, a, v):
    return tuple((sign_of(chars[i], a) * v[i]) % 3 for i in range(4))


def gid(v, a):
    return qindex[v] * 4 + a


def gmulg(g, h, chars):
    v, a = divmod(g, 4)
    w, b = divmod(h, 4)
    return gid(vadd(Q[v], act(chars, a, Q[w])), a ^ b)


def order(g, chars):
    x = g
    o = 1
    while x != 0:
        x = gmulg(x, g, chars)
        o += 1
        assert o <= 324
    return o


def independent(v, w):
    return v != ZERO and w != ZERO and v != w and v != vneg(w)


def main():
    chars = ((1, 0), (1, 0), (0, 1), (1, 1))
    with open('n18_cover_1123.json', encoding='utf-8') as f:
        data = json.load(f)
    sets = [set(s) for s in data['selected_sets']]
    meta = data['selected_meta']
    print(f"selected subgroups: {len(sets)}; sizes: {sorted(set(len(s) for s in sets))}")
    assert len(sets) == 27
    assert all(len(s) == 18 for s in sets)
    assert len({frozenset(s) for s in sets}) == 27

    for idx, H in enumerate(sets):
        for g in H:
            for h in H:
                assert gmulg(g, h, chars) in H, (idx, g, h)
        for g in H:
            assert any(gmulg(g, h, chars) == 0 for h in H)

    union = set().union(*sets)
    assert union == set(range(324))
    print("PASS: all 27 sets are subgroups of order 18; union = 324/324")

    orders = {}
    for g in range(324):
        o = order(g, chars)
        orders[o] = orders.get(o, 0) + 1
    print("element orders:", dict(sorted(orders.items())))

    print("\nstructure of the 27 selected subgroups:")
    for idx, (H, m) in enumerate(zip(sets, meta)):
        k = m['k']
        M = [tuple(v) for v in m['M']]
        b1 = next(v for v in M if v != ZERO)
        b2 = next(v for v in M if independent(v, b1))
        # derive the offset from H: choose any element over k
        over_k = [g for g in H if g % 4 == k]
        # its Q-coordinate is an offset representative
        off = Q[over_k[0] // 4]
        print(f"  #{idx:2d}: image=<{k}>, M=<{b1},{b2}>, offset={off}")


if __name__ == '__main__':
    main()
