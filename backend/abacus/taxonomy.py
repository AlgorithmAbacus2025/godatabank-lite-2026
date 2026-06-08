"""Deterministic taxonomy rules for Abacus v0.1."""

from __future__ import annotations


REGIONS = (
    "Global",
    "Europe",
    "North America",
    "South America",
    "Africa",
    "Asia-Pacific",
    "Middle East",
)

SECTORS = (
    "Economy",
    "Employment",
    "Education",
    "Healthcare",
    "Immigration",
    "Trade",
    "Technology",
    "Environment",
    "Governance",
    "Infrastructure",
    "Finance",
)

REGION_RULES = (
    ("Asia-Pacific", ("asia-pacific", "asia pacific", "east asia", "south asia", "southeast asia", "pacific", "oceania")),
    ("Middle East", ("middle east", "mena", "gulf", "levant")),
    ("North America", ("north america", "united states", "canada", "mexico")),
    ("South America", ("south america", "latin america", "caribbean", "brazil", "argentina", "chile", "colombia", "peru")),
    ("Africa", ("africa", "sub-saharan", "saharan", "maghreb")),
    ("Europe", ("europe", "european", "euro area", "eurozone")),
    ("Global", ("global", "worldwide", "international", "multi-country", "all countries")),
)

SECTOR_RULES = (
    ("Finance", ("finance", "financial", "bank", "banking", "correspondent banking", "credit", "grant", "monetary")),
    ("Economy", ("economy", "economic", "gdp", "growth", "inflation", "macroeconomic")),
    ("Employment", ("employment", "labour", "labor", "jobs", "wage", "workforce")),
    ("Education", ("education", "school", "student", "learning", "literacy")),
    ("Healthcare", ("health", "healthcare", "hospital", "disease", "medical")),
    ("Immigration", ("immigration", "migration", "migrant", "refugee", "asylum")),
    ("Trade", ("trade", "export", "import", "tariff", "customs")),
    ("Technology", ("technology", "digital", "ict", "broadband", "software")),
    ("Environment", ("environment", "climate", "emissions", "pollution", "biodiversity")),
    ("Governance", ("governance", "government", "public sector", "policy", "procurement")),
    ("Infrastructure", ("infrastructure", "transport", "road", "rail", "energy", "water")),
)

TOPIC_RULES = (
    ("Banking", ("correspondent banking", "banking", "bank")),
    ("Procurement", ("procurement plan", "procurement")),
    ("Grant", ("grant",)),
    ("Project Finance", ("project finance", "financing", "loan", "credit")),
    ("Economic Growth", ("economic growth", "growth", "gdp")),
    ("Employment", ("employment", "jobs", "labour", "labor")),
    ("Education", ("education", "school", "student", "learning")),
    ("Healthcare", ("healthcare", "health", "hospital", "medical")),
    ("Migration", ("migration", "immigration", "migrant", "refugee")),
    ("Trade", ("trade", "export", "import", "tariff")),
    ("Technology", ("technology", "digital", "ict", "broadband")),
    ("Environment", ("environment", "climate", "emissions", "pollution")),
    ("Governance", ("governance", "government", "policy")),
    ("Infrastructure", ("infrastructure", "transport", "road", "energy", "water")),
)

STOPWORDS = {
    "a",
    "an",
    "and",
    "for",
    "from",
    "in",
    "no",
    "of",
    "on",
    "or",
    "the",
    "to",
    "with",
}
