# Formalization status

**No Lean formalization is currently provided.** Neither manuscript has a
verified, theorem-mapped Lean development in the source packages inspected for
this release. In particular, no project-specific Lean source, pinned Lean
toolchain, Lake project, or compiled proof artifact was found. No Lean proof
build was performed because there was no manuscript proof project to build.

## What exists

The following are research materials and computational checks, not Lean
formalizations:

- The anomalous-Abelian-boundary manuscript has a TeX source, analytic notes,
  and Python checks. For example, `verify_czx.py` tests finite CZX rings and
  encoded blocks, while `check_zn_negativity.py` checks finitely many cyclic
  groups and cuts. Those checks do not prove the all-size statements.
- The CFT-reconstruction manuscript has a TeX source, analytic notes, and
  Python checks. For example, `verify_neighbor_seeds.py` checks explicit
  Narain-code seeds and their first composition; the Bell-recursion and
  angular-reconstruction checks cover finite cases. These checks do not by
  themselves prove the all-parameter reconstruction or physical realization
  statements.

This audit covered the two manuscript work directories, their relevant
supporting research/check directories and staging material, and the user-facing
source-and-checks ZIP files for the two manuscripts. Their ZIP inventories
contain no `.lean`, Lean toolchain, Lake configuration, or compiled Lean proof
artifact. This is a statement about the inspected material, not a search of
every file or external repository.

Lean 4.34.1 and Lake 5.0.0-src+5045d00 were available in the local environment
when checked. They are not included as a verified manuscript project, and an
installed compiler does not certify a mathematical claim.

## Bounded future targets

These are proposals only; none is supplied or verified here.

1. **Graph parity and the NPT minor.** Formalize the finite Eulerian-graph
   cut-parity lemma and the algebraic determinant of the displayed
   three-by-three partial-transpose minor, with explicit hypotheses on the
   phase and group order. This would not by itself formalize the entanglement
   convex roof, the orbit decomposition, or the anomaly interpretation.
2. **Finite gluing algebra.** Formalize the binary isotropic-code hypotheses
   and the Bell-gluing/coset-enumerator identity used for the CFT sharpness
   construction, with a theorem-by-theorem mapping to the paper. Check the
   named finite seeds separately. This alone would not establish their CFT
   realization or the full modular-reconstruction theorem.
3. **Polynomial uniqueness sublemma.** Formalize a polynomial zero-counting
   lemma with the orbit and degree assumptions stated explicitly. Connecting
   those assumptions to a torus partition function, modularity, analytic
   continuation and physical spectra would remain a separate task.

Any future Lean release should pin its toolchain and dependencies, provide
reproducible build commands, identify the exact paper claims corresponding to
each proved theorem, and disclose any axioms or unproved assumptions.

## Release metadata

The inspected manuscript sources do not identify paper authors. The inspected
source packages and staging material do not contain a `CITATION.cff` or an
explicit project license. Authorship, citation metadata, and licensing are
pending decisions; no authors, rights, license terms, or repository links
should be inferred from this file. The bibliography lists authors of cited
work, not authors of these drafts.
