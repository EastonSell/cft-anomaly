# Prior-art comparison

This is a bounded comparison based on the existing research notes, prepared
for the frozen manuscript versions identified in [REVIEW_GUIDE.md](REVIEW_GUIDE.md).
It is not a complete search, a novelty determination, or external specialist
review. An equivalent result may exist under different terminology or in a
source not inspected. Section and equation numbers below refer to the linked
sources.

## Finite thermodynamic reconstruction

* [Ashrafi and Loran, *Non-chiral 2d CFT with integer energy levels*](https://arxiv.org/html/1607.08516),
  §§4–5: their chiralization and Corollary 4.3 describe thermal,
  spin-summed data, while §5.1, Eqs. (103)–(105), gives explicit full
  partition functions with equal thermal traces and different angular
  dependence. In particular, the diagonal `D4_1^2` and `E8_1` example
  predates this manuscript. Tensoring both with a common `D4_1` factor
  gives the `k=1` thermal example used in the draft. Their analysis of the
  full angular function uses additional assumptions including real-valuedness;
  it should not automatically be identified with the candidate's no-parity
  theorem.
* [Dymarsky and Shapere, *Quantum stabilizer codes, lattices, and CFTs*](https://arxiv.org/html/2009.01244),
  §6.8 near Eq. (386), gives physical code/Narain examples with identical
  thermal traces and different angular traces. The existence of a physical
  thermal-only ambiguity is therefore established prior work. Their fully
  isospectral examples should be distinguished from pairs that differ only
  when angular information is retained.
* [Kaidi and Perlmutter, *Discreteness and integrality in conformal field theory*](https://arxiv.org/html/2008.02190),
  §2.2 and Theorem 2.1, use independent-variable continuation and a
  theta-subgroup argument. Their §4.2 Result 4.2 is a different spectral
  determination statement involving an infinite low-twist region, not the
  finite set of sampled moments asserted here. Their §6 discusses limitations
  on determination by low-dimensional data for broader classes.
* [Benjamin et al., *Harmonic analysis of 2d CFT partition functions*](https://arxiv.org/html/2107.10744),
  §4.4, reconstructs from light, scalar, and spin-one spectral input under
  assumptions on the cuspidal eigenspectrum; that input is not the same as
  finitely many exact thermal spin moments.

The candidate's proposed distinction is the specific finite-temperature
and angular-order reconstruction bound, with its stated all-`k` physical
sharpness construction. The older thermal ambiguities and modular-function
methods are antecedents; this comparison does not establish that the precise
bound or construction is new. The manuscript's sharpness claim should be
checked against the current all-`k` gluing proof rather than older notes
that predate it.

## Anomalous-symmetry entanglement

* [Lessa, Cheng and Wang, *Mixed-State Quantum Anomaly and Multipartite Entanglement*](https://arxiv.org/html/2401.17357),
  PRX 15, 011069 (2025), Appendix A: the equal-weight CZX convex-roof
  constant `3 h((2+sqrt(2))/4)/2` was already **conjectured** there.
  The paper supplies a candidate attaining basis and a corresponding upper
  bound for the sector projector. Its qualitative anomaly-enforced
  tripartite nonseparability is already a theorem. The new manuscript
  proposes a matching lower proof and weighted Eulerian-graph extension;
  neither the constant nor the earlier basis should be attributed to it.
* Immediately after Eq. (23), Lessa, Cheng and Wang state an **expectation**
  that their bipartite-product eigenbasis construction extends to `Z_N` and
  finite Abelian groups. It is not a theorem. If the candidate cyclic NPT
  calculation is correct, the displayed representative contradicts that
  broad expectation for a complete product eigenbasis; it does not contradict
  a proved result or show that all representatives have the same negativity.
* [Santos and Wang](https://arxiv.org/html/1310.8291), Eq. (9), and
  [Wang, Santos and Wen](https://arxiv.org/html/1403.5256), Eqs. (25)–(27),
  are sources for the cyclic domain-wall boundary action. The phase
  conventions differ: the manuscript states an explicit on-site/generator
  relation between its branch and the polynomial branch of Eq. (27). That
  relation and charge relabeling are part of the requested review.
* [Baumgartner, Hiesmayr and Narnhofer](https://arxiv.org/html/quant-ph/0606083),
  Eqs. (52)–(54) and Theorem 5, analyze partial transpose of two-qutrit
  Bell-diagonal states and noncollinear triples. The cubic used for the
  candidate qutrit orbit block follows by specializing their general formula;
  the isolated Bell-block calculation is established prior work. The
  candidate additionally identifies the many-body orbit blocks and their
  weights for the specified sector projector. [Derkacz and Jakóbczyk](https://arxiv.org/html/0707.1575),
  §II and Eq. (III.3), also discuss line versus triangle Bell mixtures.
* [Wehner and Winter](https://arxiv.org/abs/0710.1185), Theorem 4, use
  anticommuting observables and entropy concavity in entropic uncertainty
  relations. [Hein, Eisert and Briegel](https://arxiv.org/abs/quant-ph/0307130),
  Proposition 3, give cut-rank formulas for pure graph states. These are
  relevant methods and context, but the latter formula is not itself the
  common-ensemble roof of the sector projector studied here.

For an additional related source, please give a direct link and the precise
section, theorem, or equation, and explain its hypotheses and overlap. An
absent search hit is not evidence that the result is unpublished.
