"""Check the Z_n type-I charge-projector partial-transpose reduction.

Finite tests supplement the exact n-by-n block formula in the research note.
"""
from itertools import product
from collections import Counter
import numpy as np
import sympy as sp


def winding(bits, n):
    total = sum((bits[(j + 1) % len(bits)] - bits[j]) % n for j in range(len(bits)))
    assert total % n == 0
    return total // n


def local_orbits(n, length):
    return [(0,) + a for a in product(range(n), repeat=length - 1)]


def formula_matrices(n, p, offset):
    h = (-offset) % n
    w = np.exp(2j * np.pi / n)
    return [
        np.array([[w ** (p * (r - x) * int((s - r - x) % n > h))
                   for x in range(n)] for r in range(n)], dtype=complex)
        for s in range(n)
    ]


def numerical_block(n, p, a, b, q):
    w = np.exp(2j * np.pi / n)
    op = np.zeros((n * n, n * n), complex)
    for x, y in product(range(n), repeat=2):
        state = tuple((a0 + x) % n for a0 in a) + tuple((b0 + y) % n for b0 in b)
        op[n * ((x + 1) % n) + (y + 1) % n, n * x + y] = w ** (p * winding(state, n))
    assert np.allclose(np.linalg.matrix_power(op, n), np.eye(n * n), atol=1e-13)
    rho = sum(w ** (-q * k) * np.linalg.matrix_power(op, k) for k in range(n)) / n**2
    pt = rho.reshape(n, n, n, n).transpose(0, 3, 2, 1).reshape(n * n, n * n)
    assert np.allclose(pt, pt.conj().T, atol=1e-13)
    return np.linalg.eigvalsh(pt)


for n in range(2, 7):
    for p in range(1, n):
        all_formula_norms = []
        for offset in range(n):
            matrices = formula_matrices(n, p, offset)
            assert all(np.allclose(h, h.conj().T, atol=1e-14) for h in matrices)
            all_formula_norms.extend(np.sum(np.abs(np.linalg.eigvalsh(h))) for h in matrices)
        target = sum(all_formula_norms) / n**3
        assert target > 1 + 1e-10 if n >= 3 else abs(target - 1) < 1e-13
        # L=3 covers singleton endpoints; L=4 covers both-endpoints-variable.
        for L in (3, 4):
            for cut in range(1, L):
                offsets = Counter()
                for a, b in product(local_orbits(n, cut), local_orbits(n, L - cut)):
                    offset = (a[-1] + b[-1]) % n
                    offsets[offset] += 1
                    expected = np.sort(np.concatenate([np.linalg.eigvalsh(m) / n**2
                                                       for m in formula_matrices(n, p, offset)]))
                    for q in (0, n - 1):
                        actual = numerical_block(n, p, a, b, q)
                        assert np.allclose(actual, expected, atol=1e-12), (n, p, L, cut, a, b, q)
                assert offsets == {offset: n ** (L - 3) for offset in range(n)}
        print("n,p,trace norm:", n, p, round(target, 12), flush=True)

print("all Z_n block tests passed for n=2..6, L=3,4")

# Independent exact arithmetic for the eight parity-inequivalent n=4 blocks.
for p in (1, 2, 3):
    negative_sum = 0
    all_values = []
    for offset in range(4):
        h = (-offset) % 4
        for s in range(4):
            matrix = sp.Matrix([[sp.I ** (p * (r - x) * int((s - r - x) % 4 > h))
                                 for x in range(4)] for r in range(4)])
            for value, multiplicity in matrix.eigenvals().items():
                assert value.is_real
                all_values.append(value)
                if value.is_negative:
                    negative_sum -= multiplicity * value
                else:
                    assert value.is_nonnegative
    norm = sp.simplify(1 + negative_sum / 32)
    minimum = -sp.sqrt(2) if p in (1, 3) else sp.Integer(-2)
    assert any(sp.simplify(value - minimum) == 0 for value in all_values)
    assert all(sp.simplify(value - minimum).is_nonnegative for value in all_values)
    expected_norm = (5 + sp.sqrt(5) + sp.sqrt(2) + 2 * sp.sqrt(3)) / 8 if p in (1, 3) else sp.Rational(3, 2)
    assert sp.simplify(norm - expected_norm) == 0
    threshold = sp.simplify(1 / (1 - minimum))
    assert threshold == (sp.sqrt(2) - 1 if p in (1, 3) else sp.Rational(1, 3))
    print("exact n=4, p, trace norm, PPT threshold:", p, norm, threshold)
