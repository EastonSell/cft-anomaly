"""Independent connected-cut Z3 charge-projector partial-transpose check.

Tests every shift-orbit pair and all charges for L=3..7, including one-site
regions, and compares full physical matrices at small L.  Symbolic checks are
exact; floating-point tests are diagnostics, not a proof for all L.
"""
from itertools import product
import collections

import numpy as np
import sympy as sp

w = np.exp(2j * np.pi / 3)


def winding(bits):
    diff = sum((bits[(j + 1) % len(bits)] - bits[j]) % 3 for j in range(len(bits)))
    assert diff % 3 == 0
    return diff // 3


def local_orbits(length):
    return [(0,) + tail for tail in product(range(3), repeat=length - 1)]


def sector_block(a, b, charge):
    u = np.zeros((9, 9), dtype=complex)
    for x, y in product(range(3), repeat=2):
        bits = tuple((z + x) % 3 for z in a) + tuple((z + y) % 3 for z in b)
        u[3 * ((x + 1) % 3) + (y + 1) % 3, 3 * x + y] = w ** winding(bits)
    assert np.allclose(u @ u @ u, np.eye(9), atol=2e-14)
    rho = (np.eye(9) + w ** (-charge) * u + w ** (-2 * charge) * u @ u) / 9
    pt = rho.reshape(3, 3, 3, 3).transpose(0, 3, 2, 1).reshape(9, 9)
    assert np.allclose(pt, pt.conj().T, atol=1e-14)
    return np.linalg.eigvalsh(pt)


# Exact Hermitian 3-by-3 block: omega and omega^2 are written explicitly.
t = sp.symbols("t")
om = (-1 + sp.sqrt(3) * sp.I) / 2
H = sp.Matrix([[1, 1, 1], [1, 1, om**2], [1, om, 1]])
poly = sp.factor(H.charpoly(t).as_expr(), extension=sp.I * sp.sqrt(3))
assert sp.simplify(poly - (t**3 - 3 * t**2 + 3)) == 0
print("exact nontrivial 3x3 characteristic polynomial:", poly)

lam = sorted((1 + 2 * np.cos(2 * np.pi / 9 + 2 * np.pi * k / 3)) / 9 for k in range(3))
nontrivial = np.sort(np.repeat(lam, 3))
trivial = np.array([0.0] * 6 + [1 / 3] * 3)
target = (5 + 8 * np.cos(np.pi / 9)) / 9

for L in range(3, 8):
    for cut in range(1, L):
        groups = collections.Counter()
        for a, b in product(local_orbits(cut), local_orbits(L - cut)):
            offset = (a[-1] + b[-1]) % 3
            groups[offset] += 1
            # All charges are checked, including the shift of the block phase.
            for charge in range(3):
                eigen = sector_block(a, b, charge)
                expected = trivial if offset == 1 else nontrivial
                assert np.allclose(eigen, expected, atol=2e-14), (L, cut, a, b, charge)
        assert groups == {0: 3 ** (L - 3), 1: 3 ** (L - 3), 2: 3 ** (L - 3)}
        print("L, cut, offsets:", L, cut, dict(sorted(groups.items())))


def full_matrix(L, charge):
    states = list(product(range(3), repeat=L))
    indices = {state: i for i, state in enumerate(states)}
    dim = 3**L
    u = np.zeros((dim, dim), dtype=complex)
    for i, state in enumerate(states):
        shifted = tuple((a + 1) % 3 for a in state)
        u[indices[shifted], i] = w ** winding(state)
    return (np.eye(dim) + w ** (-charge) * u + w ** (-2 * charge) * u @ u) / dim


for L in (3, 4, 5):
    M = 3 ** (L - 2)
    predicted = np.sort(np.array([1 / (3 * M)] * M + [0.0] * (2 * M)
                                 + sum(([ev / M] * (2 * M) for ev in lam), [])))
    for charge in range(3):
        rho = full_matrix(L, charge)
        for cut in range(1, L):
            da, db = 3**cut, 3 ** (L - cut)
            pt = rho.reshape(da, db, da, db).transpose(0, 3, 2, 1).reshape(da * db, da * db)
            eigen = np.linalg.eigvalsh(pt)
            assert np.allclose(eigen, predicted, atol=2e-14), (L, cut, charge)
            assert abs(np.sum(abs(eigen)) - target) < 2e-13
    print("full-matrix spectra passed for L=", L)

# Exceptional two-site test: only offset zero is available.
two_site = sector_block((0,), (0,), 0)
assert np.allclose(two_site, nontrivial, atol=2e-14)
assert abs(sum(abs(two_site)) - (1 + 4 * np.cos(np.pi / 9)) / 3) < 2e-14
print("two-site exception: only offset 0; trace norm", sum(abs(two_site)))
print("connected-cut trace norm for L>=3:", target)
