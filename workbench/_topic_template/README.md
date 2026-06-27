# ALIS-Lite Topic Template

This folder is a template for one evidence-response topic.

Copy this folder and rename the copy using a lowercase topic slug, for example:

`workbench/uk_migration_ten_years/`

One topic folder should contain one evidence chain only.

Publication is separate and must not happen automatically.

## Workflow

1. Record the story trigger in `story_scan.md`.
2. Convert the story into a research question.
3. Plan official sources in `source_plan.md`.
4. Customise `fetch.py` for the topic.
5. Save raw evidence in `fetched/`.
6. Save source records in `source_records/`.
7. Customise `analyse.py` only after evidence exists.
8. Save analysis outputs in `analysis/`.
9. Draft the report in `draft_reports/`.
10. Use `verification.md` before any publication decision.

## Core rule

Breaking stories are signals, not evidence.

Official sources are evidence.

Analysis begins only after the evidence chain exists.