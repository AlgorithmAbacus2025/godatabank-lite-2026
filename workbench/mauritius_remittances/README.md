# Mauritius Remittances Workbench

This folder contains the evidence-response workbench for personal remittances received as a percentage of GDP in Mauritius.

It follows the GoDataBank Lite manual workbench topic structure.

## Topic Workflow

1. **Trigger**: Story signal captured in [story_scan.md](file:///c:/Users/kmudh/Documents/GoDataBank-Lite-2026/workbench/mauritius_remittances/story_scan.md).
2. **Planning**: Sources planned in [source_plan.md](file:///c:/Users/kmudh/Documents/GoDataBank-Lite-2026/workbench/mauritius_remittances/source_plan.md).
3. **Fetch**: Execute [fetch.py](file:///c:/Users/kmudh/Documents/GoDataBank-Lite-2026/workbench/mauritius_remittances/fetch.py) to save raw responses in `fetched/` and source records in `source_records/`.
4. **Analyse**: Execute [analyse.py](file:///c:/Users/kmudh/Documents/GoDataBank-Lite-2026/workbench/mauritius_remittances/analyse.py) to produce `analysis/analysis.json`.
5. **Draft**: Narrative report drafted in [draft_reports/report.md](file:///c:/Users/kmudh/Documents/GoDataBank-Lite-2026/workbench/mauritius_remittances/draft_reports/report.md).
6. **Verify**: Human verification logged in [verification.md](file:///c:/Users/kmudh/Documents/GoDataBank-Lite-2026/workbench/mauritius_remittances/verification.md) before publication.
7. **Draft Preview**: Local HTML preview generated at [reports/report.html](file:///c:/Users/kmudh/Documents/GoDataBank-Lite-2026/workbench/mauritius_remittances/reports/report.html).

## Core Rule

* Breaking stories are signals, not evidence.
* Official sources are evidence.
* Analysis begins only after the evidence chain exists.
