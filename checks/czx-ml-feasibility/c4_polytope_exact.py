"""Independently enumerate the C4 edge-polytope vertices over rationals.

Run with ``python -B c4_polytope_exact.py``.  Standard library only.
"""
from fractions import Fraction as F
from itertools import combinations, product

N = 4
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))


def solve(rows):
    """Solve four affine equalities by exact Gaussian elimination."""
    a = [[F(x) for x in coefficients] + [F(rhs)] for coefficients, rhs in rows]
    for col in range(N):
        pivot = next((i for i in range(col, N) if a[i][col]), None)
        if pivot is None:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        q = a[col][col]
        a[col] = [v / q for v in a[col]]
        for i in range(N):
            if i != col:
                q = a[i][col]
                a[i] = [v - q * w for v, w in zip(a[i], a[col])]
    return tuple(a[i][-1] for i in range(N))


def main():
    inequalities = []  # a*x <= b
    for i in range(N):
        unit = tuple(int(j == i) for j in range(N))
        inequalities.append((unit, 1))
        inequalities.append((tuple(-a for a in unit), 0))
    for i, j in EDGES:
        inequalities.append((tuple(int(k == i or k == j) for k in range(N)), 1))
    vertices = set()
    tested = 0
    for active in combinations(inequalities, N):
        tested += 1
        x = solve(active)
        if x is not None and all(sum(a * z for a, z in zip(row, x)) <= b
                                 for row, b in inequalities):
            vertices.add(x)
    expected = {tuple(map(F, x)) for x in product((0, 1), repeat=N)
                if all(x[i] + x[j] <= 1 for i, j in EDGES)}
    if vertices != expected or len(vertices) != 7:
        raise ValueError(f'vertex mismatch: {vertices} vs {expected}')
    print(f'{tested} active-constraint combinations checked exactly')
    print(f'{len(vertices)} vertices; exactly the 0/1 independent sets of C4')
    print('maximal vertices: (1, 0, 1, 0), (0, 1, 0, 1)')
    print('C4 pairwise outer polytope is integral; checks passed')


if __name__ == '__main__':
    main()
