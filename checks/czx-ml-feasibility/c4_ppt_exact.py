"""Exact PPT-strengthened C4 replica cut; not an entropy-bound improvement.

Run with ``python -B c4_ppt_exact.py``.  This uses only integers and
fractions.  See README for the analytic dual-certificate interpretation.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement

import c4_exact as exact


def main():
    d = 8
    labels = list(combinations_with_replacement(range(d), 2))
    phases = [exact.phase(a) for a in range(d)]
    # In normalized sector basis e_a, Omega = sum_a phases[a] e_a e_a / sqrt(d).
    # Eight times (|Omega><Omega|)^Gamma is a signed swap. Verify its
    # Hermiticity and involution explicitly, then its upper bound by 1.
    signed_swap = [[0] * (d*d) for _ in range(d*d)]
    for a in range(d):
        for b in range(d):
            signed_swap[b*d+a][a*d+b] = phases[a] * phases[b]
    if any(signed_swap[i][j] != signed_swap[j][i] for i in range(d*d) for j in range(d*d)):
        raise ValueError('partial-transpose signed swap is not symmetric')
    for i in range(d*d):
        for j in range(d*d):
            if sum(signed_swap[i][k]*signed_swap[k][j] for k in range(d*d)) != int(i == j):
                raise ValueError('partial-transpose signed swap is not an involution')
    upper = [[int(i == j)-signed_swap[i][j] for j in range(d*d)] for i in range(d*d)]
    if exact.ldlt_positive_semidefinite(upper) is None:
        raise ValueError('PPT fidelity operator bound rejected')
    print('exact PPT fidelity bound: <Omega|rho|Omega> <= 1/8')
    for sign in (1, -1):
        gram, mat = exact.matrices(sign, (1, 1, 1, 1))
        # For unnormalized t_aa=v_a⊗v_a, <t_aa|Omega>=phase(a)/sqrt(2).
        # Therefore the Omega projector has entries phase(a)phase(b)/2
        # on the diagonal-label block and zero elsewhere.
        projector = [[F(phases[a]*phases[c], 2) if a == b and c == e else F(0)
                      for c, e in labels] for a, b in labels]
        dual = [[(3*gram[i] if i == j else 0)-mat[i][j]+projector[i][j]
                 for j in range(len(gram))] for i in range(len(gram))]
        result = exact.ldlt_positive_semidefinite(dual)
        if result is None:
            raise ValueError('3I-H+|Omega><Omega| is not PSD')
        pivots, zeros = result
        # A deliberately excessive 6/5 spectral-gap subtraction must fail.
        negative = [[(F(14,5)*gram[i] if i == j else 0)-mat[i][j]
                     + F(6,5)*projector[i][j]
                     for j in range(len(gram))] for i in range(len(gram))]
        if exact.ldlt_positive_semidefinite(negative) is not None:
            raise ValueError('invalid 6/5 gap control was accepted')
        print(f'sector {sign}: exact 3I-H+|Omega><Omega| PSD; '
              f'{len(pivots)} positive, {zeros} zero pivots')
        print('invalid 6/5 spectral-gap control rejected')
    print('valid PPT cut: sum x_i <= 25/8, strictly better than replica spectral 4')
    print('NO entropy-bound improvement: existing edge inequalities give sum x_i <= 2')


if __name__ == '__main__':
    main()
