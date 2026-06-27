# Source Plan

## Status

Source planning stage. No analysis yet.

## Research question

How significant are personal remittances received in Mauritius when measured as a percentage of GDP, according to World Bank data?

## Primary source 1

Institution: World Bank

Dataset/document: World Development Indicators (WDI) API

API URL or source URL: https://api.worldbank.org/v2/country/MUS/indicator/BX.TRF.PWKR.DT.GD.ZS?format=json&per_page=100

Reason for use: Provides official intergovernmental annual time series for personal remittances received as a percentage of GDP.

Expected fields: `indicator`, `country`, `countryiso3code`, `date`, `value`.

Limitations: The WDI series relies on reporting by country authorities; 2025 values are currently null/preliminary.

Admission decision: Approved. Admitted under World Bank WDI source admission rules.

## Sources excluded

None.

## Fetch decision

Approved for fetch: Yes

Reviewer: K M

Date: 2026-06-24
