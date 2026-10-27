"""Finite-size numerical diagnostics for z3_negativity_note.md.

The proof is in the note. This script constructs the lattice action directly,
checks all charge sectors and connected cuts through L=5, and checks the
alternating L=4 and L=6 disconnected examples. It requires NumPy.
"""

from itertools import product
import numpy as np


OMEGA = np.exp(2j * np.pi / 3)
XI = np.exp(2j * np.pi / 9)
TARGET = (5 + 8 * np.cos(np.pi / 9)) / 9
ALT_TARGET = (1 + 4 * np.cos(np.pi / 9)) / 3


def basis_index(xs):
    index = 0
    for x in xs:
        index = 3 * index + x
    return index


def boundary_action(length):
    size = 3**length
    U = np.zeros((size, size), dtype=complex)
    for xs in product(range(3), repeat=length):
        shifted = tuple((x + 1) % 3 for x in xs)
        phase = sum((xs[(j + 1) % length] - xs[j]) % 3 for j in range(length))
        assert phase % 3 == 0
        U[basis_index(shifted), basis_index(xs)] = XI**phase
    return U


def sector_state(U, q):
    return (np.eye(U.shape[0]) + OMEGA ** (-q) * U + OMEGA ** (-2 * q) * (U @ U)) / U.shape[0]


def partial_transpose(rho, length, A):
    axes = list(range(2 * length))
    for site in A:
        axes[site], axes[length + site] = axes[length + site], axes[site]
    return rho.reshape((3,) * (2 * length)).transpose(axes).reshape(rho.shape)


def norm_pt(rho, length, A):
    return np.sum(np.abs(np.linalg.eigvalsh(partial_transpose(rho, length, A))))


def block_action(s):
    V = np.zeros((9, 9), dtype=complex)
    for a, b in product(range(3), repeat=2):
        d = (b - a) % 3
        f = (d + (s - d) % 3 - s) // 3
        V[3 * ((a + 1) % 3) + (b + 1) % 3, 3 * a + b] = OMEGA**f
    return V


for s in range(3):
    V = block_action(s)
    assert np.allclose(V @ V @ V, np.eye(9))
    expected = 1 if s == 2 else ALT_TARGET
    for q in range(3):
        sigma = sector_state(V, q)
        assert np.allclose(np.trace(sigma), 1)
        assert np.allclose(norm_pt(sigma, 2, [0]), expected)
print("Two-qutrit orbit-block norms and all charge sectors verified.")

for length in range(3, 6):
    U = boundary_action(length)
    assert np.allclose(U @ U @ U, np.eye(U.shape[0]))
    for q in range(3):
        rho = sector_state(U, q)
        assert np.allclose(np.trace(rho), 1)
        assert np.allclose(U @ rho, OMEGA**q * rho)
        for cut in range(1, length):
            norm = norm_pt(rho, length, range(cut))
            assert np.isclose(norm, TARGET, atol=1e-11)
    print(f"All connected cuts and charges verified at L={length}.")

U3 = boundary_action(3)
ket = np.zeros(27, dtype=complex)
for a, b in product(range(3), repeat=2):
    ket[basis_index((a, b, (b + 1) % 3))] = 1 / 3
assert np.allclose(U3 @ ket, OMEGA * ket)
print("Strongly symmetric connected-cut product-state counterexample verified.")

for length, A, expected in [
    (4, (0, 2), ALT_TARGET),
    (5, (0, 2), TARGET),
    (6, (0, 2, 4), 1.0),
]:
    rho = sector_state(boundary_action(length), 0)
    norm = norm_pt(rho, length, A)
    assert np.isclose(norm, expected, atol=1e-11)
    print(f"Disconnected cut L={length}, A={A}: norm={norm:.15f}")

print("All Z3 finite-size diagnostics passed.")
