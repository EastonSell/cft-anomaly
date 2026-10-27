"""Exact finite checks for a proposed bowtie-graph qualitative-gap argument.

No model, external solver, or paid service. The mathematical proof that the
all-half vertex is unattainable is in the companion work-only note; this script
checks its finite graph identities, polytope enumeration, and one witness.
"""
from fractions import Fraction as F
from itertools import combinations, product

N = 5
EDGES = ((0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 0))
WEIGHTS = (2, 1, 1, 1, 1)


def solve(rows):
    a = [[F(x) for x in row] + [F(b)] for row, b in rows]
    for col in range(N):
        pivot = next((j for j in range(col, N) if a[j][col]), None)
        if pivot is None:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        a[col] = [x / a[col][col] for x in a[col]]
        for j in range(N):
            if j != col:
                scale = a[j][col]
                a[j] = [x - scale*y for x, y in zip(a[j], a[col])]
    return tuple(a[j][-1] for j in range(N))


def bit(z, i):
    return (z >> (N-1-i)) & 1


def q(z):
    return sum(bit(z, i)*bit(z, j) for i, j in EDGES)


def symmetry(v):
    # i^6=-1, and X^5 complements all five bits.
    out = [0] * 32
    for z, amplitude in enumerate(v):
        out[31 ^ z] = -(-1)**q(z) * amplitude
    return out


def main():
    inequalities = []
    for i in range(N):
        unit = tuple(int(j == i) for j in range(N))
        inequalities.extend(((unit, 1), (tuple(-x for x in unit), 0)))
    for i, j in EDGES:
        inequalities.append((tuple(int(k == i or k == j) for k in range(N)), 1))
    vertices = set()
    for active in combinations(inequalities, N):
        x = solve(active)
        if x is not None and all(sum(a*z for a, z in zip(row, x)) <= b
                                 for row, b in inequalities):
            vertices.add(x)
    binary = {v for v in vertices if all(x in (0, 1) for x in v)}
    expected_binary = {tuple(map(F, v)) for v in product((0, 1), repeat=N)
                       if all(v[i] + v[j] <= 1 for i, j in EDGES)}
    fractional = vertices - binary
    half = (F(1, 2),)*N
    if len(vertices) != 17 or binary != expected_binary or len(binary) != 10 or len(fractional) != 7:
        raise ValueError('unexpected exact vertex set')
    if half not in fractional or any(any(x > F(1,2) for x in v) for v in fractional):
        raise ValueError('all-half vertex does not dominate fractional vertices')
    if max(sum(w*x for w, x in zip(WEIGHTS, v)) for v in binary) != 2:
        raise ValueError('unexpected weighted independent-set value')
    print('4368 active sets: 17 vertices, 10 binary and 7 fractional')
    print('all-half dominates all fractional vertices; best binary reward = 2')

    # Four even sets: empty, {0,1}, {2,3}, {0,1,2,3}.
    z01 = (1 << 4) | (1 << 3)
    z23 = (1 << 2) | (1 << 1)
    phase = (-1)**sum(q(z) for z in (0, z01, z23, z01 | z23))
    if phase != -1:
        raise ValueError('phase obstruction has disappeared')
    print('parity-class quadratic phase product = -1; linear phases cancel')

    # |+>_0 tensor (|0000>-|1111>)_{1,2,3,4}, unnormalized.
    witness = [int((z & 15) == 0)-int((z & 15) == 15) for z in range(32)]
    if symmetry(witness) != witness or sum(z*z for z in witness) != 4:
        raise ValueError('positive-sector witness failed')
    neg = [(-1 if bit(z, 0) else 1)*a for z, a in enumerate(witness)]
    if symmetry(neg) != [-a for a in neg]:
        raise ValueError('negative-sector witness failed')
    for site in range(N):
        mask = 1 << (N-1-site)
        xx = F(sum(witness[z]*witness[z ^ mask] for z in range(32)), 4)
        zz = F(sum(((-1)**bit(z, site))*witness[z]**2 for z in range(32)), 4)
        expected = 1 if site == 0 else 0
        if xx != expected or zz != 0:
            raise ValueError('witness local marginal failed')
    print('both sector witnesses pass; x=(1,0,0,0,0), entropy = 4 ln 2')
    print('NO certified PPT improvement or quantitative physical gap is claimed')


if __name__ == '__main__':
    main()
