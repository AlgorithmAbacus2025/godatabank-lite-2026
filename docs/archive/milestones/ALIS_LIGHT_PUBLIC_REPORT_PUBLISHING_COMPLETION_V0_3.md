# ALIS-Light Public Report Publishing v0.3 — Completion Note

**Date:** 1 July 2026  
**Status:** Ready for the existing GitHub → Cloudflare Pages workflow

## Public root and selected report

The existing Cloudflare Pages public payload is `site/`. The repository contains
a tracked `site/index.html`, and no repository deployment configuration was
found that overrides this output root.

The selected existing generated report is:

`reports/generated/world-bank-40107522.html`

The source report was not regenerated or modified.

## Minimum publishing change

- Added an exact copy at `site/reports/world-bank-40107522.html`.
- Added one homepage permalink in `site/index.html` pointing to
  `/reports/world-bank-40107522.html`.

`reports/manifest.json` already identifies the selected generated report, so no
manifest change was required.

## Checks

- The generated source and public report SHA-256 hashes match.
- The homepage contains the expected report link.
- The linked target exists under `site/`.
- The public report contains no unresolved template placeholders.
- `git diff --check -- site` passes.

## Changed files

- `site/index.html`
- `site/reports/world-bank-40107522.html`
- `docs/ALIS_LIGHT_PUBLIC_REPORT_PUBLISHING_COMPLETION_V0_3.md`

No backend, validator, publisher, workbench, recovery, generated-report,
manifest, or deployment files were changed by this milestone. Existing
uncommitted changes elsewhere in the working tree were preserved.

## Expected public URL

`https://godatabank.com/reports/world-bank-40107522.html`

No commit, push, or deployment was performed.
