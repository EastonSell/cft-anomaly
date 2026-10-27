# Bowtie-graph qualitative gap: candidate target for a stronger certificate

**Status.** This is a local mathematical preflight for the synthetic five-vertex graph below. The analytic argument and its finite integer/rational checks require independent specialist review. They do not give a numerical lower bound on the gap, identify the physical optimum, certify an improving PPT cut, or evaluate an ML system. The universal no-go for the original nonnegative two-copy spectral menu still applies.

Let `G` have edges `01,12,20,03,34,40` (two triangles sharing vertex 0), and let `S=i^6 X_0...X_4 ∏ CZ_ij=−X_0...X_4 ∏ CZ_ij`. Fix either sector `Sψ=λψ`, λ=±1. Put `x_i=<X_i>²+<Y_i>²` and take weights `w=(2,1,1,1,1)`. The pairwise outer polytope is `0≤x_i≤1`, `x_i+x_j≤1` on edges. The entropy objective is `F_w(x)=Σ_i w_i f(x_i)`, with `f(x)=h((1+√x)/2)` in nats and `h(p)=−p ln p−(1−p) ln(1−p)`.

## The relaxed minimizer

The companion exact-rational script enumerates the 4,368 five-active-constraint sets, obtaining 17 vertices: the 10 binary independent-set vectors and seven fractional vectors. Every fractional vertex has all coordinates at most one half, and the all-half vector `x*=(1/2,...,1/2)` is among them. Since all weights are positive and f decreases strictly, x* has strictly smaller objective than every other fractional vertex. For binary vertices the maximum total selected weight is 2, so the best objective is `4 ln 2`.

For `r=√x`, the positive power series

`ln 2−f(x)=Σ_(n≥1) x^n/[2n(2n−1)]`

gives `f(1/2)≤ln 2−1/4`. Since `ln 2<3/4`, `6 f(1/2)≤6 ln 2−3/2<4 ln 2`. The latter logarithm inequality follows by integrating the strict upper chord `1/x < 3/2−x/2` on `1<x<2`. Therefore x* uniquely minimizes among vertices. By concavity of f and the convex-hull representation of the bounded polytope, x* is also the unique global relaxed minimizer, with value `6 f(1/2)`.

## The all-half point is not physical

Suppose to the contrary that a sector state has every `x_i=1/2`. Let `M_i` be the normalized local XY observable aligned with its Bloch vector. Then `M_i²=I` and `<M_i>=1/√2`. For each edge ij, `A_i=S M_i S` anticommutes with `M_j`; each is a Hermitian involution. Sector symmetry gives `<A_i>=1/√2`, so `(A_i+M_j)²=2I` and `<A_i+M_j>=√2` force

`(A_i+M_j)|ψ>=√2|ψ>`.

Comparing two neighbors j and k of the same i yields `M_j|ψ>=M_k|ψ>`. Vertex 0 has all four leaves as neighbors, so their M actions agree; comparing the two neighbors 0 and 2 of vertex 1 brings the center into the same class. The five local M observables commute across sites. Their equal-action conditions therefore put ψ in the span of the two all-equal product eigenvectors. For angles θ_i, ψ has computational amplitudes

`ψ(z)=2^(−5/2) exp(i θ·z) [a+b (−1)^|z|]`.

S complements all five bits, so a nonzero sector eigenstate must have nonzero amplitudes in both parity classes; hence both `a+b` and `a−b` are nonzero. Define `q(z)=Σ_(ij in E) z_i z_j` modulo 2. Comparing the sector equation at different bit strings z within one fixed parity class then forces

`g(z)=(−1)^q(z) exp(−2i θ·z)`

to be constant on that class. Take the four even sets `∅`, `{0,1}`, `{2,3}`, and `{0,1,2,3}`. Their quadratic phases are respectively `+1,−1,+1,+1`, and the linear phases cancel in

`g({0,1}) g({2,3}) / [g(∅) g({0,1,2,3})] = −1`.

Constancy would instead make this ratio +1, a contradiction. This is a mathematical proof conditional on the stated graph-sector encoding; the companion script checks its finite phase identity, not the entire analytic inference.

The normalized unit sphere in either finite-dimensional sector is compact, and F_w is continuous. Its physical minimum is attained. Since it cannot occur at x*, the unique relaxed minimizer, its value is **strictly greater** than `6 f(1/2)`. This is a qualitative positive gap, with no computed magnitude. The explicit plus-sector state `|+>_0 (|0000>−|1111>)_(1,2,3,4)/√2` has `x=(1,0,0,0,0)` and value `4 ln 2`; applying `Z_0` gives a witness in the minus sector. Thus the physical optimum is no larger than `4 ln 2`, but equality is not established.

## Reproduction and research implication

From the repository root, or from the root of a standalone copy of this staged tree, run:

```text
python -B checks/czx-ml-feasibility/czx_bowtie_exact.py
```

Python 3.9+ and the standard library suffice. The script checks the rational vertex set, weighted binary objective, quadratic-phase obstruction, involution action on both witnesses, and exact local marginals. No network, model inference, SDP solver, or paid service is used.

If independently confirmed, the bowtie gives a relevant open target for a **different, quantitative, checked** bound. It does not itself provide such a bound or improve the existing PPT certificate. Before a learned search is considered, require a specific valid cut or relaxation with a verified positive improvement over the pairwise entropy bound, a physical witness, and deterministic solvers given the same constraints and complete resource budget. One synthetic structural example is not evidence of generalization or novelty over prior moment/SOS work.
