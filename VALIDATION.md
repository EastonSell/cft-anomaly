# Local release-candidate validation

Validation performed on 2026-10-27 against a fresh copy of `v0.1.0-draft.1`:

- The release checker verified 63 SHA-256 entries and 71 local Markdown links in the initial assembled copy. The final manifest can be checked again with `python scripts/verify_release.py`; it intentionally does not claim to check external URLs or heading anchors.
- All six documented CFT checks passed with Python 3.11.15. These include exact seed and finite recursion checks, not an enumeration of all values of `k`.
- All six anomaly diagnostics passed with Python 3.11.15, NumPy 2.4.3, SymPy 1.14.0 and mpmath 1.3.0 in an isolated environment; `pip check` reported no broken requirements. They include both exact finite calculations and floating-point matrix tests.
- All five ML-note checks passed with Python 3.11.15 and the standard library. They confirm the documented finite certificates and controls, not an ML result.
- The frozen PDF and TeX source hashes matched the [release manifest](RELEASE_MANIFEST.md). From the fresh copy, Tectonic 0.17.0 using an existing cached TeX bundle rebuilt the CFT manuscript as three pages and the anomaly manuscript as four pages. No overfull boxes, unresolved citations or undefined references appeared in the final logs. Nonfatal underfull-box, BibTeX-style and Fontconfig notices were emitted. The supplied PDFs had previously been rendered and visually inspected.
- The per-project checksum manifests were checked independently. Of 31 external Markdown URLs, 30 returned successful HTTP HEAD responses; the remaining APS page returned HTTP 403 to HEAD but opened successfully in a browser. This is a link-availability check, not a complete priority audit.

These checks establish the stated reproduction and file-integrity results only. They are not an independent human review, a Lean formalization, a proof of every all-parameter claim, a determination of research priority, or evidence of journal acceptance.
