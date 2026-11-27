# ALIS-Light ONS Fertility Report v0.5 — Completion Note

**Date:** 2 July 2026  
**Status:** Ready for the existing GitHub → Cloudflare Pages workflow

## Public report

Created:

`site/reports/england-wales-fertility-birth-cohort-2024.html`

Expected public URL:

`https://godatabank.com/reports/england-wales-fertility-birth-cohort-2024.html`

The homepage now presents the ONS fertility report as the latest report. The
Mauritius GDP per capita report and earlier World Bank technical record remain
linked and were not deleted.

## Evidence boundary

The GovDelivery newsletter was used only to locate the ONS release. No figure,
claim, interpretation, or limitation in the public report is sourced from the
newsletter.

Evidence sources:

1. ONS statistical bulletin, **Fertility for those born in different years,
   England and Wales: 2024**, released 10 June 2026.
2. ONS dataset, **Fertility for those born in different years, England and
   Wales**, latest XLSX released 10 June 2026.
3. ONS quality and methods guide for the cohort-fertility release series.

The official ONS workbook was downloaded to the new workbench:

`workbench/england_wales_fertility_birth_cohort_2024/fetched/ons_fertility_birth_cohort_2024.xlsx`

- Size: 686,877 bytes.
- SHA-256: `FECC464EBEA5EE23116512C76AD7D5E7921FD6CF51A3A2C6E42E620078B37757`.
- Retrieved: 2 July 2026 at 09:14:37 UTC.

## Verified figures

The downloaded workbook was imported and inspected by worksheet and cell.

- Women born in 1925: observed completed family size 2.12,
  `Table 1a!AF14`.
- Women born in 1953: observed completed family size 2.05,
  `Table 1a!AF42`.
- Women born in 1979: observed completed family size 1.95,
  `Table 1a!AF68`.
- Men born in 1979: achieved family size 1.82 through age 45,
  `Table 5!AF40`.
- Men born in 1959: observed completed family size 2.00,
  `Table 5!AZ20`.
- Women born in 1959: observed completed family size 1.98,
  `Table 1a!AF48`.
- Women born in 2008: projected completed family size 1.48,
  `Table 1b!AF98`.
- Girls born in 2026: projected completed family size 1.43,
  `Table 1b!AF116`.

The ONS bulletin supplies the reported 15.7% childlessness share for women born
in 1979 and the ages at which the 1979 cohorts averaged one child: 31 years for
women and 33 years for men.

## Public interpretation and limits

The report states that selected observed female cohorts had progressively
smaller completed family sizes and reached the one-child milestone later. It
labels the 2008 and 2026 cohort values as projections.

The report also records that:

- national population projections are scenarios, not forecasts;
- later cohorts have not completed their reproductive years;
- completed family size counts live-born children;
- birth-cohort year is approximate;
- male cohort statistics are official statistics in development; and
- cohort averages do not describe every individual or the distribution within
  a cohort.

## Changed files

- `workbench/england_wales_fertility_birth_cohort_2024/README.md`
- `workbench/england_wales_fertility_birth_cohort_2024/source_plan.md`
- `workbench/england_wales_fertility_birth_cohort_2024/source_records/source.json`
- `workbench/england_wales_fertility_birth_cohort_2024/analysis/analysis.json`
- `workbench/england_wales_fertility_birth_cohort_2024/verification.md`
- `workbench/england_wales_fertility_birth_cohort_2024/fetched/.gitkeep`
- `workbench/england_wales_fertility_birth_cohort_2024/fetched/ons_fertility_birth_cohort_2024.xlsx`
- `site/reports/england-wales-fertility-birth-cohort-2024.html`
- `site/index.html`
- `docs/ALIS_LIGHT_ONS_FERTILITY_REPORT_COMPLETION_V0_5.md`

## Checks completed

- Official ONS bulletin and dataset URLs are present in the report.
- The newsletter URL is absent from the public report.
- ONS workbook sheet structure and selected source cells were inspected.
- Downloaded workbook hash matches the workbench source record.
- Workbench JSON files parse successfully.
- Homepage and report HTML parse successfully.
- Homepage-to-report navigation returned HTTP 200 in the local public root.
- Desktop rendering and semantic heading structure were checked.
- Existing Mauritius and technical reports remain present.
- No unresolved template placeholders remain.
- `git diff --check` passes for the v0.5 paths.

No backend, validator, publisher, existing workbench, report manifest,
template, architecture, authentication, database, or deployment file was
changed by this milestone. Pre-existing working-tree changes outside v0.5 were
preserved.

No commit, push, or deployment was performed.
