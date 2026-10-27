# Review guide for the two candidate manuscripts

These are research manuscripts, with analytic arguments and supporting
finite checks. Independent human specialist review and a complete priority
assessment remain open. The comparison in [PRIOR_ART.md](PRIOR_ART.md) is a
bounded literature assessment, not a certification of priority. The
manuscripts describe their use of AI assistance.

## Locate the versions under review

* [Finite thermodynamic reconstruction of an integer-spectrum CFT](../preprints/cft-reconstruction/README.md):
  [paper](../preprints/cft-reconstruction/paper.pdf),
  [TeX source](../preprints/cft-reconstruction/source/main.tex),
  [supporting material](../checks/cft-reconstruction/). The frozen source
  SHA-256 is `2153eb02753afc93b97bcd160a83ecb5e8949ab3cc03d69a4eae2de2f910b3f3`.
* [Quantitative mixed-state entanglement for anomalous Abelian boundaries](../preprints/anomalous-symmetry-entanglement/README.md):
  [paper](../preprints/anomalous-symmetry-entanglement/paper.pdf),
  [TeX source](../preprints/anomalous-symmetry-entanglement/source/main.tex),
  [supporting material](../checks/anomalous-symmetry-entanglement/). The frozen
  source SHA-256 is `0bd1fd4c52dac5144b421816ebfd933e53d580faaa8207b6a5c4969d8ccd884d`.

In a review, identify the commit or release and the manuscript source or PDF
hash, plus a page, equation, source label, or proof step. If the material is
revised, the frozen hashes above identify the versions this guide describes.

## Mathematical checkpoints

**CFT reconstruction.** The hypotheses include a compact unitary bosonic
theory with a unique vacuum, discrete finite-multiplicity spectrum,
`c_L=c_R=12k` for positive integral `k`, integral total dimensions and
spins, and unmultiplied full modular invariance. Reviewers can focus on:

1. The continuation to independent upper-half-plane variables, the separate
   `Gamma(2)` transformations, and all three cusp bounds used for the
   rational form `eq:form`. The proof assumes neither parity nor rationality.
2. The diagonal-orbit root count, including the self-dual orbit, and the
   common-vacuum treatment of orders zero and one. Check the distinct
   temperature conditions and the reduced-sampling statement in the theorem.
3. The low-energy corollary and the neighboring-code construction in
   `eq:k1`–`eq:product`: do both seed pairs define physical Narain CFTs,
   and does the composition establish the stated first changed level and
   angular order for every `k`?

The inputs are exact, **unnormalized**, descendant-inclusive state-spin
traces `M_r(t)`, including the ordinary thermal partition function. The
claimed result determines the torus partition function and its state
degeneracies, not OPE coefficients. It does not establish numerical stability
or claim that its sufficient number of temperatures is minimal. Finite code
and coefficient checks support the algebra but do not prove the all-`k`
claims by enumeration.

**Anomalous Abelian boundaries.** Reviewers can focus on:

1. The complement-orbit reduction for a finite loopless Eulerian multigraph,
   the pairwise Bloch inequalities `bloch`, the entropy concavity step, and
   the saturation bases in `balanced` and `bellbasis`. The mixed-state
   quantity is a **single common-ensemble convex roof**, and strong symmetry
   means support in one charge sector. The finite-range anomaly interpretation
   additionally requires the geometric hypotheses stated in the paper.
2. For the displayed cyclic action `Zn`, check the published-branch
   transformation, endpoint anomaly, and the product-witness argument leading
   to `ZnW` and `ZnE3`.
3. For sector projectors `sector`, check local orbit labels, their weights,
   the partial-transpose minor `minor`, the best-separable-weight argument,
   and the qutrit norm `Z3norm`. These claims concern the specified
   representative on a ring with `L>=3`, nonzero `p mod N`, and a connected
   nonempty bipartition; the NPT statement requires `N>=3`.

The graph statement alone does not assume spatial locality. The cyclic NPT
claim concerns sector projectors, not every state in a sector; it does not
assert that negativity is invariant under arbitrary local-circuit changes of
symmetry representative. A complete product eigenbasis is excluded for the
specified cyclic representative, although individual product eigenvectors
can exist. Finite calculations do not replace the general analytic proofs.

## Reports and contributions

Independent checks and formalization contributions are welcome. To make a
report actionable, use one of the templates in
[`.github/ISSUE_TEMPLATE`](../.github/ISSUE_TEMPLATE/) and include the exact
version, theorem or equation, and enough detail to check the argument. A
related-literature report is particularly useful when it states the source's
precise assumptions and whether it proves the same result or supplies a
methodological ingredient. The per-paper READMEs give build and check
instructions; attach the command, environment, and output for reproduction
failures.
