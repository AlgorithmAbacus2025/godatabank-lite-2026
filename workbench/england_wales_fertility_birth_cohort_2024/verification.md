# Verification Note

## Source boundary

- The GovDelivery newsletter was used only as a discovery lead.
- All published evidence comes from the official ONS bulletin, XLSX dataset,
  and quality and methods guide.

## Dataset integrity

- Downloaded file: `ons_fertility_birth_cohort_2024.xlsx`
- Size: 686,877 bytes
- SHA-256: `FECC464EBEA5EE23116512C76AD7D5E7921FD6CF51A3A2C6E42E620078B37757`
- XLSX ZIP signature: `50-4B-03-04`

## Workbook checks

The workbook contains the ONS cover, contents, notes, women’s observed and
projected cohort tables, and the new male cohort tables.

Checked cells:

- `Table 1a!AF14`: 2.12, observed completed family size for women born in 1925.
- `Table 1a!AF42`: 2.05, observed completed family size for women born in 1953.
- `Table 1a!AF68`: 1.95, observed completed family size for women born in 1979.
- `Table 5!AF40`: 1.82, achieved family size through age 45 for men born in 1979.
- `Table 5!AZ20`: 2.00, completed family size for men born in 1959.
- `Table 1a!AF48`: 1.98, completed family size for women born in 1959.
- `Table 1b!AF98`: 1.48, projected completed family size for women born in 2008.
- `Table 1b!AF116`: 1.43, projected completed family size for girls born in 2026.

## Publication limits

- Observed and projected figures must remain clearly separated.
- National population projections are scenarios based on assumptions, not
  forecasts or policy predictions.
- Male cohort fertility is published as official statistics in development.
- Completed family size covers live-born children and does not include
  stillbirths, adopted, fostered, or stepchildren.
- Cohort averages do not describe every individual or the distribution of
  family sizes.

Publication decision: approved for the scoped ALIS-Light v0.5 public report.
