# Source Plan

## Status

Source planning stage. No analysis yet.

## Research question

What does World Bank data show about Mauritius GDP per capita over time?

## Primary source 1

Institution: World Bank

Dataset/document: World Development Indicators (WDI) API

API URL or source URL: https://api.worldbank.org/v2/country/MUS/indicator/NY.GDP.PCAP.CD?format=json&per_page=100

Reason for use: Provides official intergovernmental annual time series for GDP per capita in current US$.

Expected fields: `indicator`, `country`, `countryiso3code`, `date`, `value`.

Limitations: Relies on official national reporting. Values for the latest year may be preliminary or revised.

Admission decision: Approved. Admitted under World Bank WDI source admission rules.

## Sources excluded

None.

## Fetch decision

Approved for fetch: Yes

Reviewer: K M

Date: 2026-06-27
