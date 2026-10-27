# Reproducibility checks

The checks are grouped by project. Run them from the repository root using the commands in each linked guide:

- [CFT-001](cft-reconstruction/README.md): standard-library exact arithmetic and finite checks of lattice-code seeds, gluing, and angular reconstruction.
- [ANOM-001](anomalous-symmetry-entanglement/README.md): exact finite identities and explicitly labeled numerical matrix diagnostics for the graph and anomalous-symmetry examples.
- [CZX ML feasibility note](czx-ml-feasibility/README.md): standard-library exact C4 and bowtie checks. These assess a proposed certificate menu; they do not evaluate an ML model.

The analytic arguments are in the papers and supporting notes. A finite check or numerical diagnostic is evidence about its stated cases, not a proof of a general theorem. The [formalization catalogue](../formalization/README.md) records the absence of a provided Lean development.
