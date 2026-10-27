"""Run the portable anomalous-boundary diagnostic suite."""
from pathlib import Path
import subprocess
import sys

import mpmath
import numpy
import sympy

HERE = Path(__file__).resolve().parent
TESTS = (
    "verify_czx.py",
    "check_general_N_blocks.py",
    "check_zn_negativity.py",
    "independent_pt_orbits.py",
    "check_published_branch.py",
    "z3_negativity_check.py",
)

print("Python", sys.version.split()[0])
print("NumPy", numpy.__version__, "SymPy", sympy.__version__, "mpmath", mpmath.__version__)
for name in TESTS:
    print("\nRUN", name, flush=True)
    result = subprocess.run([sys.executable, name], cwd=HERE, text=True,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(result.stdout, end="", flush=True)
    print("EXIT", result.returncode, flush=True)
    if result.returncode:
        raise SystemExit(result.returncode)
print("\nAll six finite diagnostics passed.")
