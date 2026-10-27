# Finite diagnostics for the anomalous-symmetry preprint

These scripts check selected finite cases and algebraic ingredients of the
candidate preprint. They do not prove its all-size results, establish priority,
or replace independent specialist review. They are portable copies of scripts
from the supplied source archive: two workspace-specific dependency lookup
lines and one obsolete note reference were removed; the checking logic was
not changed.

The recorded run used **Python 3.11.15**, NumPy **2.4.3**, SymPy **1.14.0**
and mpmath **1.3.0**. From the release bundle root, in an activated Python
3.11 virtual environment, run:

```text
cd checks/anomalous-symmetry-entanglement
python -m pip install -r requirements.txt
python run_all.py
```

Run without Python's `-O` flag because the checks use assertions. Dense matrix
diagonalizations may take longer on some systems. All six diagnostics exited
successfully from a fresh extraction in an isolated environment with the
versions above; `pip check` reported no broken requirements. The final runner
line was `All six finite diagnostics passed.`

| Script | Scope and arithmetic |
| --- | --- |
| `verify_czx.py` | Exact integer-valued complex arithmetic for encoded Pauli identities, candidate bases, and even rings through `L=10`; the printed entropy is floating point. |
| `check_general_N_blocks.py` | Floating-point block matrices for `n=3,...,8`, every nonzero `p`, and every holonomy; tests the displayed minors and NPT bounds. |
| `check_zn_negativity.py` | Floating-point orbit blocks for `n=2,...,6`, `L=3,4` and selected charges, plus exact SymPy calculations for `n=4`. |
| `independent_pt_orbits.py` | Exact SymPy qutrit cubic; floating-point orbit checks through `L=7` and full matrices through `L=5`, across all connected cuts and charges. |
| `check_published_branch.py` | Floating-point checks of both phase conventions for small `n`, lengths, charges and connected cuts. The all-size branch identity is analytic, not established by these tests. |
| `z3_negativity_check.py` | Floating-point qutrit sector checks through `L=5` and selected disconnected cuts, including an alternating `L=6` PPT example. PPT alone does not prove separability. |

The frozen preprint and build instructions are in
`../../preprints/anomalous-symmetry-entanglement/`.
