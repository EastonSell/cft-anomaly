# CZX-inspired ML feasibility: offline research note

This package is a **research note, not a NeurIPS result**. No model study was run, and no cut has been demonstrated to improve the starting entropy bound. The candidate physics and the general no-go argument require independent specialist and priority review.

The original nonnegative two-copy spectral menu is redundant under the stated graph and sector assumptions. The C4 exact check gives a spectral bound of 4 where existing edge constraints imply 2. The separately checked PPT bound of 25/8 improves that loose spectral bound but is still weaker than 2; it is not a demonstrated entropy improvement or the claimed PPT optimum. A bowtie argument offers a possible qualitative target, but supplies no numerical gap, physical optimum, or improving PPT certificate.

- [Research note](assessment.md): assumptions, proof, prior work, and the future experiment gate.
- [C4 derivation and exact certificates](docs/c4_audit.md).
- [Bowtie qualitative-gap argument](docs/bowtie_qualitative_gap.md): the finite script does not verify the full analytic proof.
- [Checks](../../checks/czx-ml-feasibility/): the unmodified standard-library Python scripts from the companion preflight archive.
- [Verification record](VERIFICATION.md): commands and observed results from a fresh copy.

## Run from the repository root

Run these commands from the repository root, or from the root of a standalone copy of this staged tree. Python **3.9 or newer** is required. Only the Python standard library is used; no network, model inference, external solver, or paid service is needed.

    python -B checks/czx-ml-feasibility/c4_exact.py
    python -B checks/czx-ml-feasibility/c4_polytope_exact.py
    python -B checks/czx-ml-feasibility/c4_independent_checks.py
    python -B checks/czx-ml-feasibility/c4_ppt_exact.py
    python -B checks/czx-ml-feasibility/czx_bowtie_exact.py

Each command must exit successfully. Expected landmarks are:

- C4 witnesses pass in both sectors; the exact two-copy spectral interval is [4,4], and the false 3999/1000 bound is rejected.
- The independent C4 polytope enumeration checks 495 active sets and finds 7 vertices; the separate checks confirm the Pauli action and logarithm enclosure.
- The exact PPT certificate gives the valid upper bound 25/8, with no improvement over the existing edge bound 2.
- The bowtie check examines 4,368 active sets and finds 17 vertices; it verifies the finite phase obstruction and both sector witnesses.

The finite checks support the stated calculations; they do not substitute for independent review of the general or bowtie proofs. SHA256SUMS lists the files as packaged.
