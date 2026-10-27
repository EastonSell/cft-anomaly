# Maintaining the repository

The research-draft collection is hosted at [EastonSell/cft-anomaly](https://github.com/EastonSell/cft-anomaly). The repository does not establish journal publication, independent verification, or priority. The snapshot version is not itself a GitHub Release or tag.

For future updates:

1. Review the proofs, provenance, prior-art comparisons and scope; independent specialist review remains open.
2. Confirm the responsible human author list and affiliations for each paper. Select a license or other reuse terms; none is assigned in this snapshot.
3. Complete and validate `CITATION.cff.template` using confirmed author metadata, then rename it to `CITATION.cff`. Update `CITATION.bib` with confirmed authors and any actual DOI. The current BibTeX entries are provisional and title-based.
4. The proposed description and topics in [REPOSITORY_METADATA.md](REPOSITORY_METADATA.md) have not been applied; decide whether to use them.
5. Work from a clone, or initialize Git with `git init -b main` if starting from an extracted source ZIP. After edits, regenerate the checksum manifest and run the release checker:

   ```sh
   python scripts/build_manifest.py
   python scripts/verify_release.py
   git add -A
   git diff --cached --stat
   git status
   ```

6. Commit and push through an authorized account. For a public release, keep an immutable artifact and checksum, record corrections in [CHANGELOG.md](CHANGELOG.md), and use a new version rather than silently replacing an archived release.

The issue templates invite review; they do not contact anyone or create issues by themselves.
