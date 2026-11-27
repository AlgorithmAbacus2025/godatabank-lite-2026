# ALIS-Light OBR Welfare Fraud and Error Report v0.6 - Completion Note

**Date:** 2 July 2026  
**Status:** Ready for the existing GitHub to Cloudflare Pages workflow

## Public report

Created:

`site/reports/uk-welfare-fraud-error-trends-2026.html`

Expected public URL:

`https://godatabank.com/reports/uk-welfare-fraud-error-trends-2026.html`

The homepage now presents this as the latest public report. The ONS fertility,
Mauritius GDP per capita, and World Bank technical reports remain linked and
were not deleted.

## Evidence source

Office for Budget Responsibility, **Welfare trends report**, June 2026,
CP 1634.

The supplied descriptive path named
`obr_welfare_trends_report_june_2026.pdf`. The actual uploaded file in that
source folder is:

`workbench/uk_welfare_fraud_error_trends_2026/source_documents/E03599306_OBR_WTR_2026_Accessible_v3.pdf`

The actual file was used without renaming or duplication.

- Pages: 45.
- Size: 567,678 bytes.
- SHA-256: `2CFCD88EEB986064C358CF99D43E891EA2EFBA035A4297D3048768399319F16E`.

No internet source was substituted for the local PDF.

## Verified evidence

The following PDF pages were extracted and visually checked:

- PDF page 1: title, June 2026, and CP 1634.
- PDF page 8, printed page 3: overall welfare rates, UC rates, and sampling
  uncertainty.
- PDF page 9, printed page 4: Covid-cohort concentration, operational
  easements, relaxed checks, and self-employment factors.
- PDF pages 10-11, printed pages 5-6: planned removal of the rising underlying
  propensity assumption and uncertainty around that judgement.
- PDF page 17, printed page 12: Covid-cohort decline from 25.8% in 2020-21 to
  8.9% in 2025-26.

Verified headline rates:

- Overall welfare fraud and error: 3.1% of spending in 2019-20, 4.3% in both
  2020-21 and 2021-22, then 3.2%.
- Universal Credit fraud and error: 9.4% of UC spending in 2019-20, 14.7% in
  2021-22, then 8.5% in 2025-26.
- Covid-cohort UC fraud and error: 25.8% in 2020-21 and 8.9% in 2025-26.

## Interpretation controls

The public report preserves the OBR's uncertainty language:

- operational easements and self-employment issues are described as a likely
  primary explanation, not proven sole causes;
- rates are identified as shares of spending, not shares of claimants;
- overall welfare, UC, and Covid-cohort rates are identified as using different
  denominators;
- the Covid cohort is defined as UC cases joining between 14 March 2020 and
  27 February 2021;
- the forecast-method change is described as planned for future forecasts; and
- sampling exercises and limited evidence on drivers are explicit limitations.

## Changed files

- `workbench/uk_welfare_fraud_error_trends_2026/README.md`
- `workbench/uk_welfare_fraud_error_trends_2026/source_records/source.json`
- `workbench/uk_welfare_fraud_error_trends_2026/analysis/analysis.json`
- `workbench/uk_welfare_fraud_error_trends_2026/verification.md`
- `site/reports/uk-welfare-fraud-error-trends-2026.html`
- `site/index.html`
- `docs/ALIS_LIGHT_OBR_WELFARE_FRAUD_ERROR_REPORT_COMPLETION_V0_6.md`

The source PDF existed before implementation and was not modified.

## Checks completed

- Local PDF metadata, page count, size, and hash checked.
- Required claims located through PDF text extraction.
- Relevant PDF pages rendered and visually compared with extracted text.
- Workbench JSON files parse successfully.
- Homepage and report HTML parse successfully.
- Every required percentage and interpretation appears in the public report.
- Homepage-to-report navigation returned HTTP 200.
- Desktop rendering, semantic heading structure, and table width were checked.
- Existing public reports remain present and linked.
- No unresolved template placeholders remain.
- `git diff --check` passes for the v0.6 paths.

No backend, validator, publisher, architecture, feature, authentication,
database, report manifest, template, or deployment file was changed by this
milestone. Pre-existing working-tree changes outside v0.6 were preserved.

No commit, push, or deployment was performed.
