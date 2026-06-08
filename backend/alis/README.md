# ALIS

## Status

ALIS v0.1 implements one official metadata retrieval path: the World Bank Documents & Reports API.

This folder does not contain AI summarisation code, databases, subscription features, publishing logic, search, Abacus implementation, or additional institution connectors.

## Purpose

ALIS is the source admission and retrieval boundary for GoDataBank. In v0.1 it fetches one World Bank publication metadata record, validates required metadata fields, stores the record as JSON, archives the retrieved metadata, and logs success or failure with a timestamp.

## v0.1 Responsibilities

ALIS v0.1 supports:

- Official World Bank API metadata retrieval
- JSON storage under `data/raw/world_bank/`
- Timestamped archive output under `data/raw/world_bank/archive/`
- Structured log output under `data/raw/world_bank/logs/`
- Validation for `title`, `institution`, `source_url`, and `publication_date`

## Admission Boundary

ALIS must reject or hold any source that fails one or more required conditions:

- Not issued by an official institution
- No public API or approved machine-readable feed
- No English content or English metadata
- Missing citation metadata
- Belongs to an excluded category
- Cannot be verified from the official source

Only admitted sources may support GoDataBank reports.

## Non-Goals

ALIS must not introduce:

- Additional institution connectors
- Databases
- Web scraping
- AI summarisation
- Abacus
- Publishing
- Search
- Paid access or subscription features
- Unofficial source aggregation
- News, vendor, think tank, blog, social media, or user-generated evidence paths
