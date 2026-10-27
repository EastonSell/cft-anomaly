# Exact C4 sector and two-copy audit

This is a deterministic finite-dimensional calculation for the synthetic four-cycle graph, not a model experiment, a CZX-chain theorem, or a claim of new physics. It uses CPU and the Python standard library only. The checker [checks/czx-ml-feasibility/c4_exact.py](../../../checks/czx-ml-feasibility/c4_exact.py) was run locally without network access. It constructs and checks the sector operators, witnesses, exact rational two-copy matrices, semidefinite certificates, and rational entropy enclosures. Domain-expert review of the mathematical interpretation remains appropriate.

## Setup and witnessed optimum

Let `C4` have sites `0,1,2,3` and edges `(0,1),(1,2),(2,3),(3,0)`. The graph is `K2,2` with parts `A={0,2}` and `B={1,3}`. Put

`S = X0 X1 X2 X3 CZ01 CZ12 CZ23 CZ30`.

It is a Hermitian involution. In an eigenstate of either sign, define `x_i=<X_i>²+<Y_i>²`. Exact operator identities checked on every computational basis vector give `<Z_i>=0` and, for every graph edge, `x_i+x_j≤1`; also `0≤x_i≤1`. Thus each single-site entropy equals `f(x_i)=h((1+sqrt(x_i))/2)` in nats, with `h(p)=−p ln p−(1−p) ln(1−p)`.

For nonnegative weights, define `W_A=w0+w2` and `W_B=w1+w3`. The edge relaxation yields and the exact witnesses attain

`min_{Sψ=±ψ} Σ_i w_i S(ρ_i) = min(W_A,W_B) ln 2`.

To see the lower bound without trusting a vertex-enumerator, for any feasible x take uniform `t∈[0,1]` and define an independent set

`I_t={i∈A: t≤x_i} ∪ {j∈B: t>1−x_j}`.

If i and j lie in opposite parts then `x_i+x_j≤1`, so they cannot both occur in `I_t`. Each site's inclusion probability is x_i. Concavity of f yields `Σ_i w_i f(x_i)≥E[Σ_i w_i f(1_{i∈I_t})]`. Since every independent set of `K2,2` is contained in A or B and f(0)=ln 2, f(1)=0, the right side is at least `min(W_A,W_B) ln 2`. This uses nonnegative weights and the already-checked qubit/symmetry hypotheses.

The plus-sector witness with pure sites A is the tensor product of `|+>` on 0 and 2 with `(|00>+|11>)/sqrt(2)` on 1 and 3. In site order `0,1,2,3`, its unnormalized computational-basis support is `{0,2,5,7,8,10,13,15}` and its norm squared is 8. The analogous witness with pure sites B has support `{0,1,4,5,10,11,14,15}` and norm squared 8. Their exact local reduced spectra are `{1,0}` on the plus sites and `{1/2,1/2}` on the Bell sites. Applying `Z0` changes sector and preserves these spectra. All four vectors are checked by the script, including a wrong-sector negative control.

Hence **no additional valid inequality can increase the edge-relaxation minimum on C4 for any nonnegative weights**: each required minimizing point is already the Bloch vector of an exact sector state. This does not say all even-degree graphs have no gap or rule out a useful controller on other graphs.

As an independent finite check of the polytope statement, `c4_polytope_exact.py` enumerates all 495 four-constraint active sets using `Fraction` arithmetic. The seven resulting vertices are precisely the empty, single-site and two maximal independent sets. Since the polytope is bounded and full-dimensional, these are all its vertices. Its output does not depend on the two-copy PSD code.

## Exact uniform two-copy spectral result

For `c=(1,1,1,1)`, the specified candidate operator is

`H = Σ_i (X_i⊗X_i + Y_i⊗Y_i)`

on two copies. Let `Π_λ` project onto the symmetric subspace of two copies of the λ sector. The sector has dimension 8, so that symmetric subspace has dimension 36. The exact calculation in each sector gives

`λ_max(Π_λ H Π_λ | ran Π_λ) = 4`.

For reproducibility, let `b=0,...,7` represent each bit string with leading bit zero, `bar b=15 xor b`, and `φ(b)=(-1)^{Σ_(ij) b_i b_j}`. The unnormalized sector basis is `v_b=|b>+λ φ(b)|bar b>`. The 36 symmetric vectors are `t_bb=v_b⊗v_b` and `t_ab=v_a⊗v_b+v_b⊗v_a` for `a<b`. Their Gram matrix D is diagonal with entries 4 and 8. The script constructs `A_ab=<t_a|H|t_b>` exactly and checks `4D−A` is positive semidefinite using rational Schur complements: 35 strictly positive pivots and one valid zero pivot. It finds an exact rational kernel vector and verifies its Rayleigh quotient is 4. The invalid proposed bound `3999/1000` is rejected. Four simple positive/indefinite matrix controls exercise the exact PSD routine.

Writing `e_b=v_b/sqrt(2)`, the maximizing two-copy state is

`|Ω> = (1/sqrt(8)) Σ_(b=0)^7 φ(b) |e_b>⊗|e_b>`.

It has Schmidt rank 8 across the two copies, so it is not `|ψ>⊗|ψ>`. The resulting valid spectral cut `Σ_i x_i≤4` is weaker than the existing edge inequalities, which add to `Σ_i x_i≤2`. This explicit separation illustrates why a spectral relaxation's eigenvector is not an attaining single-copy witness.

## Why the proposed cut menu fails on every stated graph

The following algebraic argument is independent of the C4 finite computation and applies to every finite simple graph with even vertex degrees and every sector λ, assuming the stated encoding. It has been independently checked within this project but has not undergone external specialist review.

Let `P=(I+λS)/2`, `A_i=P X_i P`, and `B_i=P Y_i P`, understood as operators on the sector `V=ran(P)` of dimension d. Since `Z_i S Z_i=−S` and `Y_i=i X_i Z_i`,

`A_i²+B_i² = P X_i [P+Z_i P Z_i] X_i P = P`.

Consequently, on `V⊗V`,

`2[I−A_i⊗A_i−B_i⊗B_i]=(A_i⊗I−I⊗A_i)²+(B_i⊗I−I⊗B_i)² ≥ 0`.

Thus the operator for any proposed nonnegative vector c is bounded above by `Σ_i c_i I`. To attain this bound, define the antiunitary `J=X_1...X_k K`, where K is computational-basis complex conjugation. Even graph degrees imply J commutes with S; J also fixes every `X_i` and `Y_i`, and `J²=I`. Choose an orthonormal J-real basis `e_1,...,e_d` of V. In that basis all A_i and B_i are real symmetric, and the symmetric two-copy vector `Ω=d^(−1/2)Σ_a e_a⊗e_a` has

`⟨Ω|(A_i⊗A_i+B_i⊗B_i)|Ω⟩=tr(A_i²+B_i²)/d=1`

for every i. Therefore the exact support value of the delivered menu is `β(c)=Σ_i c_i` for **every** `c_i≥0`. This cut is already implied by `x_i≤1`, even before adding edge constraints. Ω is a legitimate vector in the symmetric two-copy space, but for d>1 is entangled across the copies and is not a tensor square of one sector state. The unrestricted symmetric spectral relaxation has discarded a necessary physical product-state constraint.

This is a structural **NO-GO** for the menu in the original proposal, not just an inconvenient C4 example. It does not establish that higher-order, explicitly separability-constrained, PPT or other relaxations fail; any such replacement requires its own verified valid inequalities and evidence of a nonzero gap improvement. Do not run the proposed model study on the original menu.

## Exact replica-PPT calibration, and its limitation

We tested one stronger but still insufficient relaxation, with no SDP solver. In either C4 sector, let ρ be a positive, trace-one two-replica state supported in the symmetric sector and satisfying `ρ^Γ≥0`, where Γ is partial transposition across the two sector copies. All physical `|ψ⟩⟨ψ|⊗|ψ⟩⟨ψ|` are feasible. In the normalized sector basis used above, Ω is maximally entangled and the exact partial transpose of `|Ω⟩⟨Ω|` is a signed swap divided by 8. The signed swap squares to I and is symmetric, so it is at most I. Consequently every PPT state has `⟨Ω|ρ|Ω⟩≤1/8`.

The standard-library checker `c4_ppt_exact.py` independently checks, in both 36-dimensional symmetric sectors, the exact rational dual matrix inequality

`3 I − H + |Ω⟩⟨Ω| ≥ 0`.

It therefore certifies the replica-PPT upper bound `tr(Hρ)≤3+1/8=25/8`. This is a **valid but not necessarily optimal** PPT upper bound and is strictly below the unconstrained spectral value 4. However, its physical cut `Σ_i x_i≤25/8` is strictly weaker than the existing edge-based `Σ_i x_i≤2`. It does not tighten the starting entropy relaxation. The exact C4 witnesses already attain that relaxation, so no sound PPT or other cut can improve its entropy optimum on this instance. The checker rejects an intentionally overoptimistic spectral-gap control; that rejection is a test of the certificate, not a proof of any optimum. No PPT improvement on a genuine nonzero-gap graph has been established, and no replacement method is recommended from this calibration alone.

## Rigorous entropy arithmetic and reproduction

For uniform unit weights the optimum is `2 ln 2`, certified in nats within

`[1.386294361119890618, 1.386294361119890619]`.

The code uses the exact positive-term identity `ln 2 = 2 Σ_(k≥0) (1/3)^(2k+1)/(2k+1)` and bounds the omitted tail by `2(1/3)^(2N+1)/((2N+1)(1−1/9))`. Only integer and `Fraction` arithmetic is used; printed decimal endpoints are rounded outward using integer division. Equality of the state and lower-bound expressions is analytic, not inferred from overlapping decimal intervals.

Requires Python 3.9 or later and only the Python standard library. From the repository root, or from the root of a standalone copy of this staged tree, run:

```text
python -B checks/czx-ml-feasibility/c4_exact.py
python -B checks/czx-ml-feasibility/c4_polytope_exact.py
python -B checks/czx-ml-feasibility/c4_independent_checks.py
python -B checks/czx-ml-feasibility/c4_ppt_exact.py
```

Observed result: both sector witnesses pass; all local Pauli conjugation checks pass; both exact two-copy spectral intervals are `[4,4]`; both invalid `3999/1000` spectral bounds are rejected; and the entropy interval above is produced. The script version tested has SHA-256 `007200d042f6723502cbc34eb59ae8f53cd5f05197280485850b82fd6515a384`.

For any future study, the deterministic baseline must receive the same richer valid-cut grammar, graph inputs, current outer minimizer, witness templates, checker and resource cap as a learned proposer. Compare fully certified gaps against a fixed-order, a gap-based and a seeded-random search as well as any available matching moment/SOS baseline; charge verification, solver setup, model inference and amortized training. A single synthetic graph does not measure generalization, and a floating-point SDP value alone is not a proof.
