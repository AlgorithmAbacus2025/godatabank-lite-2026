"""Configuration for the ALIS v0.1 World Bank metadata connector."""

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

WORLD_BANK_INSTITUTION = "World Bank"
WORLD_BANK_API_BASE_URL = "https://search.worldbank.org/api/v3/wds"
WORLD_BANK_LANGUAGE = "English"
WORLD_BANK_API_FIELDS = (
    "display_title",
    "docdt",
    "url",
    "lang",
    "docna",
    "repnb",
    "pdfurl",
)

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw" / "world_bank"
ARCHIVE_DIR = RAW_DATA_DIR / "archive"
LOG_DIR = RAW_DATA_DIR / "logs"

LATEST_METADATA_PATH = RAW_DATA_DIR / "latest_metadata.json"
LOG_FILE_PATH = LOG_DIR / "world_bank_connector.log"

DEFAULT_TIMEOUT_SECONDS = 30
USER_AGENT = "GoDataBank-ALIS-v0.1 (official World Bank metadata retrieval)"
