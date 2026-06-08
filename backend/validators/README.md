# Validators

## Status

Validator v0.1 validates one ALIS metadata record and writes approved metadata to `data/validated/`.

This folder does not contain API connectors, AI summarisation code, databases, subscription features, publishing logic, search, Abacus, or source ingestion logic.

## Purpose

Validators are the policy enforcement boundary between ALIS and future analysis systems. Validator v0.1 checks whether an ALIS metadata record satisfies the required institutional, schema, URL, and date rules.

## v0.1 Validation Areas

Validator v0.1 checks:

- Official-institution status
- Required fields: `institution`, `title`, `publication_date`, `source_url`, `document_id`
- Publication date validity
- Source URL validity
- Approved institution status
- World Bank domain validation
- Metadata structure against `backend/validators/schema.py`

## Required Blocking Conditions

A validator must block publication when:

- Required metadata fields are missing or empty.
- The publication date is invalid.
- The source URL is invalid.
- The institution is not approved.
- A World Bank record does not use a `worldbank.org` source URL.
- The metadata structure does not match the Validator v0.1 schema.

## Non-Goals

Validators must not introduce:

- Source connectors in this milestone
- Databases
- Private or paid data access paths
- Web scraping
- AI-generated summaries
- Abacus
- Publishing
- Search
- Subscription logic
- Additional institutions
- Acceptance of news, commercial vendor, think tank, blog, social media, user-generated, or unsourced evidence
