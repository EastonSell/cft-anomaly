"""Write the SHA-256 inventory for this local release, using only Python 3."""
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED_DIRS = {'.git', '.venv', '__pycache__', 'build'}
EXCLUDED_SUFFIXES = {'.pyc', '.pyo', '.aux', '.bbl', '.blg', '.fdb_latexmk',
                     '.fls', '.log', '.out', '.synctex.gz', '.xdv'}


def release_files():
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file() or path == ROOT / 'SHA256SUMS.txt' or path.name == '.DS_Store':
            continue
        rel = path.relative_to(ROOT)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if any(path.name.endswith(suffix) for suffix in EXCLUDED_SUFFIXES):
            continue
        yield path


def main():
    lines = [f'{sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}'
             for path in release_files()]
    (ROOT / 'SHA256SUMS.txt').write_bytes(('\n'.join(lines) + '\n').encode('utf-8'))
    print(f'Wrote SHA256SUMS.txt for {len(lines)} release files.')


if __name__ == '__main__':
    main()
