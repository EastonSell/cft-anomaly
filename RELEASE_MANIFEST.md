# Release manifest

- **Version:** `v0.1.0-draft.1`
- **Status:** research-draft snapshot
- **Prepared:** 2026-10-27

The two manuscripts are the frozen source and PDF versions listed below. They are AI-assisted research drafts with analytic arguments, finite computational checks, and no independent expert review recorded. A full priority assessment remains open.

| Item | Path | SHA-256 of frozen file |
| --- | --- | --- |
| CFT-001 PDF | `preprints/cft-reconstruction/paper.pdf` | `0c298ba0873b1d157a590fe7bb57ff0aff7d9572844719198e570e6b01ad708b` |
| CFT-001 LaTeX | `preprints/cft-reconstruction/source/main.tex` | `2153eb02753afc93b97bcd160a83ecb5e8949ab3cc03d69a4eae2de2f910b3f3` |
| CFT-001 bibliography | `preprints/cft-reconstruction/source/references.bib` | `1fdce23d3bee1e5701d5606ee3e81e7275c7b17e372c622598e88f4f84e08327` |
| ANOM-001 PDF | `preprints/anomalous-symmetry-entanglement/paper.pdf` | `99b47ea6c6905d7fe17910064591e5252294e712c7ada3f83c72107c33c87542` |
| ANOM-001 LaTeX | `preprints/anomalous-symmetry-entanglement/source/main.tex` | `0bd1fd4c52dac5144b421816ebfd933e53d580faaa8207b6a5c4969d8ccd884d` |

`SHA256SUMS.txt` inventories the complete release files except the checksum file itself. `scripts/verify_release.py` checks its entries and local Markdown links. Individual checks and their dependencies are described in `checks/`; finite checks are not substitutes for the all-parameter arguments. There are no Lean formalizations in this release.

The repository is [EastonSell/cft-anomaly](https://github.com/EastonSell/cft-anomaly). No human author names, affiliations, DOI, or license are asserted. The GitHub description and topics in `REPOSITORY_METADATA.md` are proposed metadata only. Superseded material is segregated in `history/`. The version label identifies this snapshot; it does not itself assert a GitHub Release or tag.

The ZIP in `downloads/` contains the initial published tree at commit `ccb3019c035d17ac9e8704788813ed2fff687aff`. It precedes the addition of that downloadable ZIP and its links. Its accompanying SHA-256 file checks the ZIP; the ZIP's own `SHA256SUMS.txt` checks the files inside it.
