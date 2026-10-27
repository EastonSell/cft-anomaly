# CFT reconstruction checks

These standard-library Python programs accompany the [preprint and its build instructions](../../preprints/cft-reconstruction/README.md). Use Python 3.9 or newer. Run from the release root after extraction; do not use `python -O`, since the programs rely on assertions.

```sh
python checks/cft-reconstruction/verify_neighbor_seeds.py
python checks/cft-reconstruction/verify_bell_recursion.py
python checks/cft-reconstruction/verify_bell_gluing.py
python checks/cft-reconstruction/verify_physical_bell_recursion.py
python checks/cft-reconstruction/angular_reconstruction_check.py
python checks/cft-reconstruction/unequal_angular_reconstruction_check.py
```

The first four check seed and Bell-gluing code identities with exact integers; the recursion and gluing scripts are the same certificate under two filenames, while the physical recursion script uses a separate seed convention. [The physical sharpness note](all_k_physical_sharpness.md) gives the all-`k` composition argument; finite enumeration alone cannot establish the infinite claim. The two angular scripts perform exact rational tests for finitely many cases; see the [angular audit](angular_reconstruction_audit.md) for the analytical argument and the separately scoped unequal-central-charge extension. These checks support the claims but do not replace expert human verification.
