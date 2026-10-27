"""Verify release hashes and local Markdown links; Python standard library only."""
from hashlib import sha256
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from build_manifest import ROOT, release_files

LINK = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')


def main():
    errors = []
    manifest = ROOT / 'SHA256SUMS.txt'
    if not manifest.is_file():
        print('Missing SHA256SUMS.txt; run python scripts/build_manifest.py first.')
        return 1
    expected = {}
    for line in manifest.read_text(encoding='utf-8').splitlines():
        try:
            digest, relative = line.split('  ', 1)
            rel = Path(relative)
            target = (ROOT / rel).resolve()
            if (not re.fullmatch(r'[0-9a-f]{64}', digest) or rel.is_absolute()
                    or ROOT.resolve() not in target.parents or relative in expected):
                raise ValueError('invalid or duplicate entry')
            expected[relative] = digest
            if not target.is_file():
                errors.append(f'Missing manifest entry: {relative}')
            elif sha256(target.read_bytes()).hexdigest() != digest:
                errors.append(f'Checksum mismatch: {relative}')
        except ValueError:
            errors.append(f'Invalid manifest entry: {line}')

    actual = {p.relative_to(ROOT).as_posix() for p in release_files()}
    for relative in sorted(actual - set(expected)):
        errors.append(f'Unlisted release file: {relative}')

    count = 0
    for md in sorted(ROOT.rglob('*.md')):
        if any(part in {'.git', '.venv', '__pycache__', 'build'} for part in md.relative_to(ROOT).parts):
            continue
        fenced = False
        for line in md.read_text(encoding='utf-8').splitlines():
            if line.lstrip().startswith(('```', '~~~')):
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in LINK.finditer(line):
                raw = match.group(1).strip().strip('<>')
                parsed = urlsplit(raw)
                if parsed.scheme or raw.startswith(('#', '//')):
                    continue
                relative = unquote(parsed.path)
                if not relative:
                    continue
                count += 1
                target = (md.parent / relative).resolve()
                if ROOT.resolve() not in (target, *target.parents) or not target.exists():
                    errors.append(f'Broken local link in {md.relative_to(ROOT).as_posix()}: {raw}')

    if errors:
        print('\n'.join(errors))
        return 1
    print(f'PASS: {len(expected)} SHA-256 entries and {count} local Markdown links.')
    print('External URLs and Markdown heading anchors are not checked.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
