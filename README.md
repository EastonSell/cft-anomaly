# CFT and Quantum Anomaly Research Preprints

**Independent review requested.** We invite researchers in conformal field theory, modular forms, quantum anomalies, and quantum information to inspect the theorem statements and proofs, reproduce the checks, and identify related or prior work. Please open an issue specifying the manuscript version, theorem or equation, and the mathematical objection, reproduction steps, or relevant reference. Corrections and clearly scoped formalization contributions are welcome. These are preliminary AI-assisted research results; internal checks are documented, while independent expert verification and priority assessment remain open. See the [review guide](review/REVIEW_GUIDE.md).

This user-owned collection contains two short research drafts and supporting artifacts. Its organization is inspired by [openai/math](https://github.com/openai/math); it is not an OpenAI publication and does not imply OpenAI affiliation or endorsement. The work was developed at the user's direction with OpenAI Codex and GPT-6.1 Terra subagents assisting with mathematical reasoning, literature searches, exact and numerical checks, and manuscript drafting. Human verification of the mathematical results has not yet been recorded. The drafts include an AI-assistance disclosure.

## Start here

1. **[CFT-001: Finite thermodynamic reconstruction of an integer-spectrum CFT](preprints/cft-reconstruction/README.md)** — the primary draft. Under the stated two-dimensional CFT assumptions, finitely many exact thermal spin moments at finitely many inverse temperatures determine the spin-resolved torus partition function. A Narain lattice gluing construction gives physical examples demonstrating sharpness of the angular-order cutoff for every allowed $k$. [PDF](preprints/cft-reconstruction/paper.pdf) · [LaTeX source](preprints/cft-reconstruction/source/main.tex) · [Checks](checks/cft-reconstruction/README.md)
2. **[ANOM-001: Quantitative mixed-state entanglement for anomalous Abelian boundaries](preprints/anomalous-symmetry-entanglement/README.md)** — a draft on CZX symmetry, Eulerian graphs and explicit anomalous $\mathbb{Z}_N$ boundary actions. It derives a weighted convex-roof bound and studies the entanglement of charge-sector projectors across stated partitions. [PDF](preprints/anomalous-symmetry-entanglement/paper.pdf) · [LaTeX source](preprints/anomalous-symmetry-entanglement/source/main.tex) · [Checks](checks/anomalous-symmetry-entanglement/README.md)

The [catalogue](CONTENTS.md) records hypotheses and verification status for each item. The [ML feasibility note](research-notes/czx-ml-feasibility/README.md) is separate from the preprint catalogue: it corrects a proposed certificate menu and does not report a NeurIPS result.

## What the evidence means

The manuscript arguments are written analytic proofs, assessed by internal AI audits. Exact-arithmetic programs check specific algebraic identities and finite examples; floating-point numerical diagnostics are labeled as such. These checks do not by themselves establish all-parameter theorems. **No Lean formalization is currently provided.** See [formalization status](formalization/README.md) for bounded possible targets.

The CFT result assumes exact, unnormalized data and does not recover OPE coefficients or establish numerical stability. The anomaly conclusions apply to the specified actions and partitions, not automatically to every representative of an anomaly class. Existing research already established important ingredients; the [prior-art comparison](review/PRIOR_ART.md) identifies those contributions and the limits of the searches. No journal acceptance, certified novelty, or independent expert validation is claimed.

## Reproduce and cite

Each preprint directory has build instructions. Begin with the [checks guide](checks/README.md) for commands and expected outcomes, and run `python scripts/verify_release.py` to verify the release checksum manifest and local links. [CITATION.bib](CITATION.bib) contains title-based provisional entries. Authorship, affiliations, DOI, journal publication date and license have not been confirmed; the [CFF template](CITATION.cff.template) is intentionally inactive until valid authorship metadata are supplied. The repository is [EastonSell/cft-anomaly](https://github.com/EastonSell/cft-anomaly). See [release metadata](REPOSITORY_METADATA.md), [release manifest](RELEASE_MANIFEST.md), and [maintenance steps](PUBLISHING.md).

The [changelog](CHANGELOG.md) records the initial local release candidate and the earlier CZX and ML-plan history. Superseded material is kept out of the main catalogue; corrections to a public release should be recorded as new versions without overwriting archived releases.
