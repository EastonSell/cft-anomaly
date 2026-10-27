# Finite thermodynamic reconstruction of an integer-spectrum CFT

[Preprint PDF](paper.pdf) · [LaTeX source](source/main.tex) · [Bibliography](source/references.bib) · [Supporting proofs and checks](../../checks/cft-reconstruction/)

**Status:** research preprint candidate; human verification remains pending. Author names have not been supplied. DOI: unassigned. The manuscript discloses the use of OpenAI Codex and GPT-6.1 Terra in the research and drafting. Priority and publication suitability have not been established.

## Claim and scope

For compact unitary bosonic two-dimensional CFTs with a unique vacuum, discrete spectrum with finite multiplicities, equal central charges `c_L = c_R = 12k` for integer `k >= 1`, integer total dimensions and spins, and unmultiplied full modular invariance, the paper proves a finite exact-data uniqueness statement for the complete torus partition function. At each sampled rescaled inverse temperature `t = beta/(2 pi)`, use the **unnormalized**, descendant-inclusive traces

`M_r(t) = Tr[J^r exp(-2 pi t (Delta-k))]`.

A sufficient set consists of all orders `0 <= r <= R_k`, where `R_k=3k` for even `k` and `R_k=3k-1` for odd `k`, at either `k` distinct `t` all in `(0,1]`, `k` distinct `t` all in `[1,infinity)`, or `2k-1` arbitrary distinct positive `t`. The paper also gives a reduced sampling scheme and a spin-resolved low-energy criterion. A Narain-lattice construction supplies physical pairs for every `k` showing that the angular-order bound and low-energy cutoff are sharp in the stated sense.

The theorem reconstructs the genus-one partition function and spin-resolved state multiplicities, not the OPE data. Exact data are assumed; the paper does not establish numerical stability or optimality of the sufficient number of inverse-temperature samples. Its distinct pairs do not establish a vanishing-primary-level counterexample. Earlier thermal/angular ambiguities and related reconstruction results are credited in the manuscript, including [Ashrafi and Loran](https://arxiv.org/abs/1607.08516), [Dymarsky and Shapere](https://arxiv.org/abs/2009.01244), and [Kaidi and Perlmutter](https://arxiv.org/abs/2008.02190).

## Build from a fresh directory

Extract or copy the complete release, keeping `source/main.tex` and `source/references.bib` together. Install a TeX distribution with REVTeX 4.2, BibTeX, amsmath, amssymb, mathtools, hyperref, and microtype. From this preprint directory:

```sh
cd source
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Alternatively, `tectonic main.tex` builds the document when Tectonic can obtain or already has its TeX dependencies. Neither a TeX distribution nor Tectonic is bundled; a first build may require network access. The supplied PDF is the frozen original; rebuilt PDFs need not be byte-identical because of toolchain and PDF metadata differences.

## Reproduce the checks

From the release root, use Python 3.9 or newer and run the commands below. No Python packages or network connection are needed. Run normal Python, not `python -O`, since the checks use assertions.

```sh
cd checks/cft-reconstruction
python verify_neighbor_seeds.py
python verify_bell_recursion.py
python verify_bell_gluing.py
python verify_physical_bell_recursion.py
python angular_reconstruction_check.py
python unequal_angular_reconstruction_check.py
```

The seed/gluing scripts check code ranks, isotropy and weight-enumerator identities with exact integers; `verify_bell_recursion.py` and `verify_bell_gluing.py` contain the same certificate under two filenames. The independent physical recursion script uses a separate seed convention. The all-k construction follows from the displayed algebraic composition proof in the manuscript and [supporting note](../../checks/cft-reconstruction/all_k_physical_sharpness.md); enumerations and checks at finitely many values of `k` support but do not prove the infinite statement. The [angular audit](../../checks/cft-reconstruction/angular_reconstruction_audit.md) includes a separately scoped unequal-central-charge extension; its finite exact-arithmetic ranks are diagnostic, not an all-k proof. Its historical discussion of physical sharpness at `k=1` predates the all-k Narain construction.

The supplied paper files are byte-identical to the frozen originals. Their SHA-256 digests are:

```text
paper.pdf             0c298ba0873b1d157a590fe7bb57ff0aff7d9572844719198e570e6b01ad708b
source/main.tex       2153eb02753afc93b97bcd160a83ecb5e8949ab3cc03d69a4eae2de2f910b3f3
source/references.bib 1fdce23d3bee1e5701d5606ee3e81e7275c7b17e372c622598e88f4f84e08327
```

## Package verification

The six checks passed with Python 3.11 from a clean extraction. A Tectonic build from that extraction produced three pages with no overfull boxes, undefined references, or undefined citations. It emitted two underfull-box notices, a REVTeX BibTeX style warning, and a missing default Fontconfig configuration message; none prevented the build. The supplied PDF was separately rendered and inspected. These checks do not replace expert human review.

[SHA256SUMS.txt](SHA256SUMS.txt) records the release-root-relative paths and hashes of the packaged paper, notes and scripts; from the release root, `sha256sum -c preprints/cft-reconstruction/SHA256SUMS.txt` checks them where that utility is available.
