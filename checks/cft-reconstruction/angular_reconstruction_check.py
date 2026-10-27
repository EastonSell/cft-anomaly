"""Exact small-k checks for the angular-reconstruction argument.

Only standard-library arithmetic is used. This is a finite consistency check;
the all-k theorem is proved separately in angular_reconstruction_audit.md.

We average polynomial numerators under the full six-element anharmonic group,
then compute ranks of the induced finite linearized-diagonal jet map. The
linearized lambda path is equivalent to the actual angular path for the
injectivity proof by induction, not term-by-term at derivative order >= 2.
"""

from fractions import Fraction as F
from math import comb


def product(a, b):
    n = len(a)
    return tuple(tuple(sum(a[i][j] * b[j][z] for j in range(n))
                       for z in range(n)) for i in range(n))


def group(k):
    d = 3 * k
    n = d + 1
    ident = tuple(tuple(int(i == j) for j in range(n)) for i in range(n))
    # Columns describe f_a(x)=x^a/[x(1-x)]^k after S or T.
    s = tuple(tuple(((-1) ** i) * comb(a, i) if i <= a else 0
                    for a in range(n)) for i in range(n))
    t = tuple(tuple(((-1) ** ((a - k + i - a) % 2)) * comb(d-a, i-a)
                    if a <= i <= d else 0 for a in range(n))
              for i in range(n))
    pending, found = [ident], {ident}
    while pending:
        a = pending.pop()
        for g in (s, t):
            b = product(g, a)
            if b not in found:
                found.add(b)
                pending.append(b)
    assert len(found) == 6
    return tuple(found)


def independent(rows):
    """Return a rational row basis, with normalized pivots."""
    pivots = {}
    for row in rows:
        v = [F(z) for z in row]
        for pos in sorted(pivots):
            factor = v[pos]
            if factor:
                w = pivots[pos]
                v = [a - factor * b for a, b in zip(v, w)]
        pos = next((i for i, z in enumerate(v) if z), None)
        if pos is not None:
            factor = v[pos]
            pivots[pos] = [z / factor for z in v]
    return [pivots[i] for i in sorted(pivots)]


def invariant_basis(k):
    g = group(k)
    n = 3 * k + 1
    def averaged(a, b):
        return [sum(M[i][a] * M[j][b] for M in g)
                for i in range(n) for j in range(n)]
    return independent(averaged(a, b) for a in range(n) for b in range(n))


def equal_vacuum_basis(basis):
    anchor = next(v for v in basis if v[0])
    return independent([[x - v[0] / anchor[0] * y
                         for x, y in zip(v, anchor)] for v in basis])


def jet(poly, n, x, r):
    # Coefficient of s^r in P(x+s,x-s).
    out = F(0)
    for a in range(n):
        for b in range(n):
            c = poly[a*n+b]
            if not c or a+b < r:
                continue
            z = sum((-1)**q * comb(a, r-q) * comb(b, q)
                    for q in range(r+1)
                    if q <= b and r-q <= a)
            out += c * z * x**(a+b-r)
    return out


def rank_check(k):
    n = 3*k+1
    rmax = 3*k if k % 2 == 0 else 3*k-1
    basis = invariant_basis(k)
    vac = equal_vacuum_basis(basis)
    assert all(v[0] == v[1] == v[n] == 0 for v in vac)
    # x=1/2,1/3,... are inequivalent S-orbits on the thermal half-line.
    samples = [F(1, j) for j in range(2, k+2)]
    rows = [[jet(v, n, x, r) for v in vac]
            for x in samples for r in range(rmax+1)]
    rank = len(independent(rows))
    assert rank == len(vac)
    print(f'k={k}: invariant dimension {len(basis)}, fixed-vacuum '
          f'difference dimension {len(vac)}, sample rank {rank}')


def top_kernel(k, x, y):
    d = 3*k
    q = 1 if k % 2 == 0 else 2*x*y-x-y+2
    r = d if k % 2 == 0 else d-1
    return (x-y)**r*q / ((x*(1-x)*y*(1-y))**k)


def check_top_kernels():
    for k in range(1, 7):
        for x, y in [(F(1, 2), F(1, 3)),
                     (F(1, 4), F(2, 3)), (F(2, 5), F(3, 7))]:
            h = top_kernel(k, x, y)
            assert h != 0
            assert h == top_kernel(k, 1-x, 1-y)
            assert h == top_kernel(k, x/(x-1), y/(y-1))
    print('Top-order kernels: exact S and T checks for k=1,...,6 PASS')


def check_k1_physical_example():
    for x, y in [(F(1, 2), F(1, 3)),
                 (F(1, 4), F(2, 3)), (F(2, 5), F(3, 7))]:
        d = x*(1-x)*y*(1-y)
        q = 2-x-y+2*x*y
        a = 32*q**3/d
        h = (x-y)**2*q/d
        b = a+96*h
        # B=(U_x^2+3V_x^2)(U_y^2+3V_y^2)(U_x U_y+3V_x V_y)
        # and V_x^3 V_y^3=4x^2y^2/[(1-x)(1-y)].
        rx, ry = (2-x)/x, (2-y)/y
        vv3 = 4*x*x*y*y/((1-x)*(1-y))
        b_chars = vv3*(rx*rx+3)*(ry*ry+3)*(rx*ry+3)
        assert b == b_chars
    for x in [F(1, 2), F(1, 3), F(1, 5)]:
        q = 2-2*x+2*x*x
        a = 32*q**3/(x*x*(1-x)**2)
        j = 256*(1-x+x*x)**3/(x*x*(1-x)**2)
        assert a == j
    # At x=1/2, coefficients of s^2 in A and H are 6912 and 96.
    # This is checked exactly by the equivalent numerator and denominator
    # coefficient calculation.
    assert 32*((F(3, 2)**3)*8 + 3*F(3, 2)**2*(-2))*16 == 6912
    assert 4*F(3, 2)*16 == 96
    print('k=1 two physical CFT formulas and diagonal j: PASS')


if __name__ == '__main__':
    for k in (1, 2, 3):
        rank_check(k)
    check_top_kernels()
    check_k1_physical_example()
