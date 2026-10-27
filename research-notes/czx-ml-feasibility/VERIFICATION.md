# Fresh-copy verification

The commands below were run on 27 October 2026 from a newly created copy of the staged tree, using Python 3.11.15 and only the standard library. All five exited with code 0. No network, external solver, paid service, or model inference was used.

The checks verify the indicated finite calculations. They do not constitute human specialist review of the analytic no-go and bowtie arguments.

## c4_exact.py

```text
python -B checks/czx-ml-feasibility/c4_exact.py
```

```text
four exact PSD controls passed
exact U^2 and all local Pauli conjugation identities passed
sector witness plus-sites (0, 2) x= (1, 0, 1, 0) norm_squared= 8
sector witness plus-sites (1, 3) x= (0, 1, 0, 1) norm_squared= 8
negative sector control rejected
ln(2) interval: ('0.693147180559945309', '0.693147180559945310')
uniform C4 entropy interval: ('1.386294361119890618', '1.386294361119890619')
sector 1 two-copy symmetric basis: 36 Gram entries [4, 8]
exact spectral enclosure: [4, 4]
exact PSD check at 4: 35 positive pivots, 1 zero pivots
maximizing two-copy vector has Schmidt rank 8, not a state tensor square
negative spectral control 3999/1000 rejected
two-copy cut sum x_i <= 4; edge inequalities imply <= 2
sector -1 two-copy symmetric basis: 36 Gram entries [4, 8]
exact spectral enclosure: [4, 4]
exact PSD check at 4: 35 positive pivots, 1 zero pivots
maximizing two-copy vector has Schmidt rank 8, not a state tensor square
negative spectral control 3999/1000 rejected
two-copy cut sum x_i <= 4; edge inequalities imply <= 2
NO-GO: for C4, bipartite-polytope vertex witnesses already attain
min(w0+w2,w1+w3)*ln(2) for every nonnegative weight vector.
Any valid extra cut keeps those witnesses, so it cannot improve L0.
```

## c4_polytope_exact.py

```text
python -B checks/czx-ml-feasibility/c4_polytope_exact.py
```

```text
495 active-constraint combinations checked exactly
7 vertices; exactly the 0/1 independent sets of C4
maximal vertices: (1, 0, 1, 0), (0, 1, 0, 1)
C4 pairwise outer polytope is integral; checks passed
```

## c4_independent_checks.py

```text
python -B checks/czx-ml-feasibility/c4_independent_checks.py
```

```text
independent exact vertex enumeration: 495 active sets, 7 vertices
four exact weighted vertex-optimum controls passed
independent exact log(2) enclosure agrees
independent exact Pauli two-copy action agrees on 256 basis states
```

## c4_ppt_exact.py

```text
python -B checks/czx-ml-feasibility/c4_ppt_exact.py
```

```text
exact PPT fidelity bound: <Omega|rho|Omega> <= 1/8
sector 1: exact 3I-H+|Omega><Omega| PSD; 35 positive, 1 zero pivots
invalid 6/5 spectral-gap control rejected
sector -1: exact 3I-H+|Omega><Omega| PSD; 35 positive, 1 zero pivots
invalid 6/5 spectral-gap control rejected
valid PPT cut: sum x_i <= 25/8, strictly better than replica spectral 4
NO entropy-bound improvement: existing edge inequalities give sum x_i <= 2
```

## czx_bowtie_exact.py

```text
python -B checks/czx-ml-feasibility/czx_bowtie_exact.py
```

```text
4368 active sets: 17 vertices, 10 binary and 7 fractional
all-half dominates all fractional vertices; best binary reward = 2
parity-class quadratic phase product = -1; linear phases cancel
both sector witnesses pass; x=(1,0,0,0,0), entropy = 4 ln 2
NO certified PPT improvement or quantitative physical gap is claimed
```

## Source provenance

This staged research note was adapted for the repository layout from the corrected assessment (source SHA-256 ce2a9aa1d03bbf34070bf8cf25c837609935ed909523784d0b55c1126307d651). The five scripts are byte-for-byte copies of the corresponding members of the supplied preflight ZIP (source SHA-256 b24825512aa2a2fb8c0e7905f2d48c6d40e4a516b7a2dcc3fe1bc0560c60480c). No upstream output was modified.
