# CZX-inspired feasibility checks

These are offline exact checks for the [CZX-inspired research note](../../research-notes/czx-ml-feasibility/README.md) and its [assessment](../../research-notes/czx-ml-feasibility/assessment.md). They are not a NeurIPS result or an ML experiment. No model study or cut improving the starting entropy bound has been demonstrated.

Python **3.9 or later** is required. All scripts use only the Python standard library; no network, external solver, model inference, or paid service is needed.

From the repository root, or the root of a standalone copy of the staged tree, run:

```text
python -B checks/czx-ml-feasibility/c4_exact.py
python -B checks/czx-ml-feasibility/c4_polytope_exact.py
python -B checks/czx-ml-feasibility/c4_independent_checks.py
python -B checks/czx-ml-feasibility/c4_ppt_exact.py
python -B checks/czx-ml-feasibility/czx_bowtie_exact.py
```

All five commands should exit with code 0. Their main expected results are:

- The C4 checker verifies witnesses in both sectors and an exact two-copy spectral interval of `[4, 4]`; the existing edge constraints already imply `sum x_i <= 2`.
- The independent C4 polytope checker examines 495 active sets and finds seven vertices. The independent checks also confirm the two-copy Pauli action and the logarithm enclosure.
- The PPT checker certifies an upper bound of `25/8`, but the existing edge bound of 2 is stronger; the test gives no improvement to the entropy bound. The PPT optimum is not claimed to equal `25/8`.
- The bowtie checker examines 4,368 active sets, finds 17 vertices, and verifies the finite phase obstruction and witnesses in both sectors. It does not establish a quantitative gap or an improving PPT cut.

The [verification record](../../research-notes/czx-ml-feasibility/VERIFICATION.md) contains the output from a fresh-copy run. The finite checks do not replace independent specialist review of the general no-go and bowtie arguments.
