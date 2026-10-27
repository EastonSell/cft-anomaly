"""Verify the two Narain gluing seeds and their Bell composition at k=3.

Only the Python standard library is required. Each D4 discriminant class is
encoded in two bits: 00 has norm 0, and 01, 10, 11 have norm 1 modulo 2.
The first n classes are left-moving, the next n right-moving.
"""

from math import comb


def wt(bits, n):
    return sum(((bits >> (2*i)) & 3) != 0 for i in range(n))


def q(bits, n):
    mask = (1 << (2*n)) - 1
    return (wt(bits & mask, n) + wt(bits >> (2*n), n)) % 2


def b(x, y, n):
    return sum((((x >> (2*i)) & 1) * ((y >> (2*i+1)) & 1)
               + (((x >> (2*i+1)) & 1) * ((y >> (2*i)) & 1)))
               for i in range(2*n)) % 2


def span(gens):
    words = [0]
    for g in gens:
        words += [x ^ g for x in words]
    assert len(set(words)) == len(words)
    return set(words)


def table(words, n):
    mask = (1 << (2*n)) - 1
    M = [[0] * (n+1) for _ in range(n+1)]
    for x in words:
        M[wt(x & mask, n)][wt(x >> (2*n), n)] += 1
    return M


def neighbor(S, a, ap, n):
    assert len(S) == 2*n - 1
    s = span(S)
    assert len(s) == 2**(2*n-1)
    assert a not in s and ap not in s and a ^ ap not in s
    assert q(a, n) == q(ap, n) == 0 and b(a, ap, n) == 1
    assert all(q(g, n) == 0 and b(g, a, n) == b(g, ap, n) == 0 for g in S)
    assert all(b(x, y, n) == 0 for x in S for y in S)
    C = s | {x ^ a for x in s}
    D = s | {x ^ ap for x in s}
    assert len(C) == len(D) == 2**(2*n) and C & D == s
    assert all(q(x, n) == 0 for x in C | D)
    return C, D


# k=2: C minus C' has character polynomial W^6.
v = (4280689, 4003343, 13490061, 15943387, 4783610, 4517512,
     8704049, 3143493, 9304945, 11135812, 2974764, 11955798)
f, p, a2, ap2 = 30, 1, v[1], 5138
S2 = tuple(g ^ (a2 if (f >> i) & 1 else 0)
           for i, g in enumerate(v) if i != p)
C2, D2 = neighbor(S2, a2, ap2, 6)
mc, md = table(C2, 6), table(D2, 6)
for i in range(7):
    for j in range(7):
        assert mc[i][j] - md[i][j] == ((-1)**i * comb(6, i) if i+j == 6 else 0)
print("k=2 seed PASS: neighboring lattices differ by W^6")

# k=1: the extended D8-diagonal code minus D4^3-diagonal is W^2 A.
diag = tuple((1 << i) | (1 << (6+i)) for i in range(6))
f, p = 10, 1
old = diag[p]
S1 = tuple(g ^ (old if (f >> i) & 1 else 0)
           for i, g in enumerate(diag) if i != p)
a1, ap1 = 5, old
C1, D1 = neighbor(S1, a1, ap1, 3)
mc, md = table(C1, 3), table(D1, 3)
for i in range(4):
    for j in range(4):
        want = (-1)**i * comb(2, i) if i+j == 2 and i <= 2 else 0
        if i+j == 4 and 1 <= i <= 3:
            want += 3 * (-1)**(i-1) * comb(2, i-1)
        assert mc[i][j] - md[i][j] == want
print("k=1 seed PASS: neighboring lattices differ by W^2 A")


def join(x, nx, y, ny):
    lx = x & ((1 << (2*nx)) - 1)
    rx = x >> (2*nx)
    ly = y & ((1 << (2*ny)) - 1)
    ry = y >> (2*ny)
    left = lx | (ly << (2*nx))
    right = rx | (ry << (2*nx))
    return left | (right << (2*(nx+ny)))


# Bell-compose the seeds.  The common hyperplane gains one generator.
H3 = tuple(join(s, 6, 0, 3) for s in S2)
H3 += tuple(join(0, 6, s, 3) for s in S1)
H3 += (join(a2 ^ ap2, 6, a1 ^ ap1, 3),)
a3 = join(a2, 6, a1, 3)
ap3 = join(a2, 6, ap1, 3)
C3, D3 = neighbor(H3, a3, ap3, 9)
mc, md = table(C3, 9), table(D3, 9)
for i in range(10):
    for j in range(10):
        want = (-1)**i * comb(8, i) if i+j == 8 and i <= 8 else 0
        if i+j == 10 and 1 <= i <= 9:
            want += 3 * (-1)**(i-1) * comb(8, i-1)
        assert mc[i][j] - md[i][j] == want
print("k=3 Bell composition PASS: neighboring lattices differ by W^8 A")
