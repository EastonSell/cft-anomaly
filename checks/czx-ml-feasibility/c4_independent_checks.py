"""Independent rational checks of the C4 witness/polytope/spectral inputs.

Uses exact rationals and a separately coded active-set enumerator. Run with
Python 3 from this directory; no third-party packages or network required.
"""
from fractions import Fraction as F
from itertools import combinations

import c4_exact as original


def solve_square(rows, values):
    n = len(rows)
    aug = [[F(x) for x in row] + [F(y)] for row, y in zip(rows, values)]
    for col in range(n):
        pick = next((i for i in range(col, n) if aug[i][col]), None)
        if pick is None:
            return None
        aug[col], aug[pick] = aug[pick], aug[col]
        pivot = aug[col][col]
        aug[col] = [x / pivot for x in aug[col]]
        for i in range(n):
            if i != col:
                coefficient = aug[i][col]
                aug[i] = [x - coefficient * y for x, y in zip(aug[i], aug[col])]
    return tuple(aug[i][-1] for i in range(n))


def independent_vertices():
    inequalities = []
    for i in range(4):
        lower = [0] * 4
        lower[i] = -1
        inequalities.append((lower, 0))
        upper = [0] * 4
        upper[i] = 1
        inequalities.append((upper, 1))
    for i, j in ((0, 1), (1, 2), (2, 3), (3, 0)):
        a = [0] * 4
        a[i] = a[j] = 1
        inequalities.append((a, 1))
    out = set()
    checked = 0
    for active in combinations(inequalities, 4):
        checked += 1
        point = solve_square([r for r, _ in active], [b for _, b in active])
        if point is None:
            continue
        if all(sum(a * x for a, x in zip(row, point)) <= bound for row, bound in inequalities):
            out.add(point)
    return out, checked


def atanh_log_bounds(q, terms):
    low = 2 * sum((q ** (2*k+1) / (2*k+1) for k in range(terms)), F(0))
    high = low + 2*q ** (2*terms+1) / ((2*terms+1)*(1-q*q))
    return low, high


def gmul(x, y):
    return x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0]


def independent_h_action_on_basis(a, b):
    out = {}
    for i in range(4):
        mask = 1 << (3-i)
        ya = (0, -1 if a & mask else 1)
        yb = (0, -1 if b & mask else 1)
        yy = gmul(ya, yb)
        coefficient = (1 + yy[0], yy[1])  # X⊗X plus Y⊗Y
        if coefficient[1] != 0:
            raise ValueError('unexpected imaginary product coefficient')
        if coefficient[0]:
            idx = (a ^ mask) * 16 + (b ^ mask)
            out[idx] = out.get(idx, 0) + coefficient[0]
    return out


def main():
    vertices, checked = independent_vertices()
    expected = {
        (F(0),F(0),F(0),F(0)),
        (F(1),F(0),F(0),F(0)),
        (F(0),F(1),F(0),F(0)),
        (F(0),F(0),F(1),F(0)),
        (F(0),F(0),F(0),F(1)),
        (F(1),F(0),F(1),F(0)),
        (F(0),F(1),F(0),F(1)),
    }
    if vertices != expected or checked != 495:
        raise ValueError('C4 vertex set differs from expected independent-set polytope')
    print('independent exact vertex enumeration: 495 active sets, 7 vertices')

    # For a binary vertex, entropy/ln(2) is the total weight of zeros.
    for weights in ((1,1,1,1), (5,2,0,3), (0,0,0,0), (0,2,0,0)):
        observed = min(sum(weights[i] * (1-v[i]) for i in range(4)) for v in vertices)
        expected_value = min(weights[0]+weights[2], weights[1]+weights[3])
        if observed != expected_value:
            raise ValueError('weighted optimum inconsistent at a control weight')
    print('four exact weighted vertex-optimum controls passed')

    # log(2)=log(3/2)+log(4/3)=2 atanh(1/5)+2 atanh(1/7).
    a, b = atanh_log_bounds(F(1,5), 24)
    c, d = atanh_log_bounds(F(1,7), 24)
    alt_lo, alt_hi = a+c, b+d
    orig_lo, orig_hi = original.ln2_interval()
    if max(alt_lo,orig_lo) > min(alt_hi,orig_hi):
        raise ValueError('independent log enclosures do not overlap')
    if original.decimal_enclosure(2*alt_lo,2*alt_hi) != ('1.386294361119890618','1.386294361119890619'):
        raise ValueError('independent decimal entropy enclosure changed')
    print('independent exact log(2) enclosure agrees')

    for a in range(16):
        for b in range(16):
            expected_action = independent_h_action_on_basis(a,b)
            actual = original.h_action({a*16+b: 1}, (1,1,1,1))
            if actual != expected_action:
                raise ValueError('Pauli action differs from independently computed X and Y products')
    print('independent exact Pauli two-copy action agrees on 256 basis states')


if __name__ == '__main__':
    main()
