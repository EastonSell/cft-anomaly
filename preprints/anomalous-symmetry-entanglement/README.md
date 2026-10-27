# Quantitative mixed-state entanglement for anomalous Abelian boundaries

This folder contains the frozen four-page candidate preprint `paper.pdf` and
its exact TeX source in `source/main.tex`. It is a research draft. Independent
human specialist verification and a complete priority assessment remain open.

## Scope and claims

The graph result concerns a finite undirected loopless Eulerian multigraph,
with a qubit at every vertex and the specified CZX-type involution. For any
partition into three nonempty parties, the parity `e` of each pairwise
crossing-edge count is common to all three pairs. The manuscript gives a
weighted tripartite entropy lower bound for states supported in one symmetry
sector and an equal value for the normalized sector projector. The weights
are nonnegative, the entropy uses natural logarithms, and the mixed-state
measure is one common-ensemble convex roof. An arbitrary graph need not be a
spatially local anomaly. For the finite-range ring construction, the stated
anomaly identification assumes `L > 2 max(S)` and three connected arcs each
at least `max(S)` sites long; its index is `sum(S) mod 2`.

The cyclic result uses the explicit type-I domain-wall action on a ring of
`L >= 3` n-level sites, with a nonzero class label `p` modulo `n`. The
partial-transpose and best-separable-weight claims concern its normalized
charge-sector projectors across two nonempty **connected** arcs, with `n >=
3`. Their asserted best separable weight is `1/n`; for `n = 3` the asserted
partial-transpose norm is `(5 + 8 cos(pi/9))/9`. Every proper subsystem of
these projectors is maximally mixed. A separate, conservative tripartite
entropy bound is stated for three nonempty connected arcs. Strong symmetry
means support in one charge sector, not merely commutation with the action.

The values depend on the displayed representatives and partitions; they are
not claimed as numerical invariants of an anomaly class under arbitrary local
circuits. The NPT result is about sector projectors, not every strongly
symmetric state. It does not by itself prove genuine multipartite
entanglement or a new finite-depth preparation obstruction.

## Prior work and provenance

[Lessa, Cheng and Wang (2025)](https://arxiv.org/abs/2401.17357) conjectured
the CZX equal-weight entropy minimum and supplied an attaining candidate;
they also established qualitative anomaly-enforced nonseparability. Their
informal expectation that a bipartite-product basis extends to finite
Abelian groups is not a theorem. The proposed cyclic example addresses a
broad reading of that expectation for its particular representative.
[Baumgartner, Hiesmayr and Narnhofer (2006)](https://arxiv.org/abs/quant-ph/0606083)
already studied the two-qutrit Bell-mixture partial-transpose blocks; the
manuscript applies such blocks to an anomalous many-site sector. The
underlying cyclic boundary action also has established prior literature cited
in the preprint.

The preprint discloses assistance by OpenAI Codex, including GPT-6.1 Terra
subagents, in derivation, literature search, checks and drafting under user
direction. Author identification is pending; no authorship or formal
certification is implied by this package.

## Source integrity and build

The PDF and TeX source are byte-identical to the supplied frozen files:

- `paper.pdf` SHA-256: `99b47ea6c6905d7fe17910064591e5252294e712c7ada3f83c72107c33c87542`
- `source/main.tex` SHA-256: `0bd1fd4c52dac5144b421816ebfd933e53d580faaa8207b6a5c4969d8ccd884d`

To build, install a TeX distribution with REVTeX 4.2, `amsmath`, `amssymb`,
`bm` and `hyperref`, then run the following inside `source/`:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is embedded. Compilation may differ across TeX
distributions and is not a proof. Portable finite diagnostics and their
dependency instructions are in `../../checks/anomalous-symmetry-entanglement/`.
