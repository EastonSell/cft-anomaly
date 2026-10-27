"""Exact finite C4 sector, two-copy PSD, and entropy certificates.

Run: python c4_exact.py
All certification uses Python integers and fractions from the standard
library. No model, quantum hardware, network, or service is used.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import gcd, lcm

N = 4
D = 1 << N
EDGES = ((0, 1), (1, 2), (2, 3), (3, 0))
PART_A = (0, 2)
PART_B = (1, 3)


def bit(b, i):
    return (b >> (N - 1 - i)) & 1


def flip(b, i):
    return b ^ (1 << (N - 1 - i))


def phase(b):
    q = sum(bit(b, i) * bit(b, j) for i, j in EDGES)
    return -1 if q % 2 else 1


def symmetry(v):
    out = [0] * D
    for b, z in enumerate(v):
        out[(D - 1) ^ b] += phase(b) * z
    return out


def sector_basis(sign):
    out = []
    for b in range(D // 2):
        v = {b: 1, (D - 1) ^ b: sign * phase(b)}
        out.append(v)
    return out


def tensor(u, v):
    return {a * D + b: x * y for a, x in u.items() for b, y in v.items()}


def symmetric_sector_basis(sign):
    base = sector_basis(sign)
    output = []
    for a, b in combinations_with_replacement(range(len(base)), 2):
        t = tensor(base[a], base[b])
        if a != b:
            for idx, z in tensor(base[b], base[a]).items():
                t[idx] = t.get(idx, 0) + z
        output.append(t)
    return output


def h_action(vec, coefficients):
    out = {}
    for idx, amplitude in vec.items():
        a, b = divmod(idx, D)
        for i, c in enumerate(coefficients):
            if bit(a, i) != bit(b, i):
                dest = flip(a, i) * D + flip(b, i)
                out[dest] = out.get(dest, 0) + amplitude * 2 * c
    return out


def dot_sparse(a, b):
    return sum(x * b.get(i, 0) for i, x in a.items())


def matrices(sign, coefficients):
    basis = symmetric_sector_basis(sign)
    gram = [dot_sparse(a, a) for a in basis]
    for i, a in enumerate(basis):
        for b in basis[:i]:
            if dot_sparse(a, b) != 0:
                raise ValueError('sector basis unexpectedly nonorthogonal')
    acts = [h_action(v, coefficients) for v in basis]
    mat = [[dot_sparse(v, acts[j]) for j in range(len(basis))] for v in basis]
    if any(mat[i][j] != mat[j][i] for i in range(len(mat)) for j in range(len(mat))):
        raise ValueError('two-copy matrix is not real symmetric')
    return gram, mat


def ldlt_positive_semidefinite(mat):
    """Exact rational Schur complements, including zero-pivot PSD cases.

    For a PSD matrix, a zero diagonal forces every entry in that row to be
    zero. Thus a nonzero remainder in a zero-pivot row is a rejection.
    """
    n = len(mat)
    if any(len(row) != n for row in mat):
        raise ValueError('PSD matrix must be square')
    if any(mat[i][j] != mat[j][i] for i in range(n) for j in range(n)):
        raise ValueError('PSD matrix must be symmetric')
    m = [[F(a) for a in row] for row in mat]
    positives = []
    zeros = 0
    for j in range(n):
        pivot = m[j][j]
        if pivot < 0:
            return None
        if pivot == 0:
            if any(m[i][j] != 0 for i in range(j + 1, n)):
                return None
            zeros += 1
            continue
        positives.append(pivot)
        for i in range(j + 1, n):
            for k in range(i, n):
                m[k][i] -= m[i][j] * m[k][j] / pivot
                m[i][k] = m[k][i]
    return positives, zeros


def psd_upper(gram, mat, beta):
    matrix = [[(beta * gram[i] if i == j else 0) - mat[i][j]
               for j in range(len(gram))] for i in range(len(gram))]
    return ldlt_positive_semidefinite(matrix)


def bilinear(vec, mat):
    return sum(vec[i] * mat[i][j] * vec[j] for i in range(len(vec)) for j in range(len(vec)))


def rayleigh(vec, gram, mat):
    den = sum(g * a * a for g, a in zip(gram, vec))
    if not den:
        raise ValueError('zero trial vector')
    return F(bilinear(vec, mat), den)


def rational_null_vector(mat):
    """RREF over Q and return a primitive integer null vector, if any."""
    n = len(mat)
    a = [[F(z) for z in row] for row in mat]
    pivot_cols = []
    row = 0
    for col in range(n):
        pivot = next((i for i in range(row, n) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        divisor = a[row][col]
        a[row] = [z / divisor for z in a[row]]
        for i in range(n):
            if i != row and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[row])]
        pivot_cols.append(col)
        row += 1
        if row == n:
            break
    free = next((j for j in range(n) if j not in pivot_cols), None)
    if free is None:
        return None
    out = [F(0)] * n
    out[free] = F(1)
    for i, col in enumerate(pivot_cols):
        out[col] = -a[i][free]
    denominator = lcm(*(x.denominator for x in out))
    integers = [int(x * denominator) for x in out]
    divisor = gcd(*(abs(x) for x in integers))
    integers = [x // divisor for x in integers]
    if any(sum(mat[i][j] * integers[j] for j in range(n)) for i in range(n)):
        raise ValueError('null vector failed exact multiplication')
    return integers


def ln2_interval(terms=24):
    # log(2) = 2 atanh(1/3); each term positive, geometric tail bound.
    q = F(1, 3)
    lo = 2 * sum((q ** (2*k+1) / (2*k+1) for k in range(terms)), F(0))
    hi = lo + 2 * q ** (2*terms+1) / ((2*terms+1) * (1-q*q))
    return lo, hi


def decimal_enclosure(lo, hi, digits=18):
    scale = 10 ** digits
    a = lo.numerator * scale // lo.denominator
    b = -((-hi.numerator * scale) // hi.denominator)
    return f'{a // scale}.{a % scale:0{digits}d}', f'{b // scale}.{b % scale:0{digits}d}'


def bell_product(plus_part, bell_part):
    if len(plus_part) != 2 or len(bell_part) != 2 or set(plus_part) | set(bell_part) != set(range(N)):
        raise ValueError('plus and Bell parts must partition the four sites')
    # Unnormalized |+>⊗|+>⊗(|00>+|11>); norm²=8.
    return [int(bit(b, bell_part[0]) == bit(b, bell_part[1])) for b in range(D)]


def local_rho(v, i):
    norm = sum(a*a for a in v)
    rho = [[F(0), F(0)], [F(0), F(0)]]
    for b in range(D):
        if bit(b, i) == 0:
            b1 = flip(b, i)
            rho[0][0] += F(v[b]*v[b], norm)
            rho[1][1] += F(v[b1]*v[b1], norm)
            rho[0][1] += F(v[b]*v[b1], norm)
            rho[1][0] += F(v[b]*v[b1], norm)
    return rho


def bloch_length_squared(rho):
    x = 2 * rho[0][1]
    z = rho[0][0] - rho[1][1]
    return x*x + z*z


def validate_witness(v, expected_sign, expected_x):
    if not any(v):
        raise ValueError('zero vector')
    if symmetry(v) != [expected_sign * z for z in v]:
        raise ValueError('not in the requested symmetry sector')
    actual_x = [bloch_length_squared(local_rho(v, i)) for i in range(N)]
    if actual_x != list(expected_x):
        raise ValueError(f'incorrect marginal Bloch lengths: {actual_x}')
    return actual_x


def phase_flip(v, i):
    return [(-1 if bit(b, i) else 1) * v[b] for b in range(D)]


def main():
    # Independent small PSD controls: positive definite, singular PSD, and
    # two distinct indefinite matrices, including zero diagonal/off-diagonal.
    if ldlt_positive_semidefinite([[2, 1], [1, 2]]) is None:
        raise ValueError('positive definite control rejected')
    if ldlt_positive_semidefinite([[1, 1], [1, 1]]) is None:
        raise ValueError('singular PSD control rejected')
    if ldlt_positive_semidefinite([[1, 2], [2, 1]]) is not None:
        raise ValueError('indefinite control accepted')
    if ldlt_positive_semidefinite([[0, 1], [1, 0]]) is not None:
        raise ValueError('zero-diagonal indefinite control accepted')
    print('four exact PSD controls passed')
    for b in range(D):
        v = [int(i == b) for i in range(D)]
        if symmetry(symmetry(v)) != v:
            raise ValueError('U² != I')
        for i in range(N):
            # Exact actions U X_i U = X_i product Z_neighbours and
            # U Y_i U = -Y_i product Z_neighbours. The common i in Y
            # is removed; all remaining quantities are integer signs.
            neighbors = [b_ if a == i else a for a, b_ in EDGES if a == i or b_ == i]
            opposite = b ^ (D-1)
            conjugate_flip_sign = phase(b) * phase(flip(opposite, i))
            neighbor_sign = (-1) ** sum(bit(b, j) for j in neighbors)
            if conjugate_flip_sign != neighbor_sign:
                raise ValueError('X conjugation identity failed')
            lhs_y_sign = conjugate_flip_sign * (-1) ** bit(opposite, i)
            rhs_y_sign = -neighbor_sign * (-1) ** bit(b, i)
            if lhs_y_sign != rhs_y_sign:
                raise ValueError('Y conjugation identity failed')
            if (-1) ** bit(opposite, i) != -(-1) ** bit(b, i):
                raise ValueError('Z conjugation identity failed')
    print('exact U^2 and all local Pauli conjugation identities passed')
    for plus, bell, expected in ((PART_A, PART_B, (1,0,1,0)), (PART_B, PART_A, (0,1,0,1))):
        state = bell_product(plus, bell)
        validate_witness(state, +1, expected)
        validate_witness(phase_flip(state, 0), -1, expected)
        print('sector witness plus-sites', plus, 'x=', expected, 'norm_squared=', sum(t*t for t in state))
        if sum(expected) != 2:
            raise ValueError('false-cut witness did not attain sum x = 2')
    try:
        validate_witness(bell_product(PART_A, PART_B), -1, (1,0,1,0))
        raise ValueError('negative control was accepted')
    except ValueError as exc:
        if str(exc) == 'negative control was accepted':
            raise
        print('negative sector control rejected')
    lo, hi = ln2_interval()
    if not lo < hi:
        raise ValueError('invalid entropy interval')
    print('ln(2) interval:', decimal_enclosure(lo, hi))
    print('uniform C4 entropy interval:', decimal_enclosure(2*lo, 2*hi))
    for sign in (+1, -1):
        for sparse in sector_basis(sign):
            state = [sparse.get(i, 0) for i in range(D)]
            if symmetry(state) != [sign * x for x in state]:
                raise ValueError('incorrect sector basis')
        gram, mat = matrices(sign, (1,1,1,1))
        print('sector', sign, 'two-copy symmetric basis:', len(gram), 'Gram entries', sorted(set(gram)))
        shifted = [[(F(4) * gram[i] if i == j else 0) - mat[i][j]
                    for j in range(len(gram))] for i in range(len(gram))]
        exact = ldlt_positive_semidefinite(shifted)
        if exact is None:
            raise ValueError('4 failed the exact PSD test')
        pivots, zero_count = exact
        vec = rational_null_vector(shifted)
        if vec is None:
            raise ValueError('no exact null vector for spectral lower bound')
        lower = rayleigh(vec, gram, mat)
        if lower != 4:
            raise ValueError('Rayleigh quotient does not saturate 4')
        labels = list(combinations_with_replacement(range(D // 2), 2))
        expected_vec = [phase(a) if a == b else 0 for a, b in labels]
        if vec != expected_vec:
            raise ValueError('unexpected structure for the exact spectral eigenvector')
        print('exact spectral enclosure: [4, 4]')
        print('exact PSD check at 4:', len(pivots), 'positive pivots,', zero_count, 'zero pivots')
        print('maximizing two-copy vector has Schmidt rank 8, not a state tensor square')
        if psd_upper(gram, mat, F(3999,1000)) is not None:
            raise ValueError('invalid sub-4 PSD bound accepted')
        print('negative spectral control 3999/1000 rejected')
        # Edge inequalities already imply sum x_i <= 2. Thus the true
        # two-copy spectral cut sum x_i <= 4 is strictly weaker.
        print('two-copy cut sum x_i <= 4; edge inequalities imply <= 2')
    print('NO-GO: for C4, bipartite-polytope vertex witnesses already attain')
    print('min(w0+w2,w1+w3)*ln(2) for every nonnegative weight vector.')
    print('Any valid extra cut keeps those witnesses, so it cannot improve L0.')


if __name__ == '__main__':
    main()
