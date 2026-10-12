
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


# Project Root Directory Anchor (ResolveAI/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """
    Centralized configuration for ResolveAI.
    Automatically loads environment variables from the .env file.
    """
    # Environment & Models
    GEMINI_API_KEY: str | None = None
    GEMINI_MODEL: str = "gemini-3.6-flash"
    EMBEDDING_MODEL_NAME: str = "all-MiniLM-L6-v2"

    # Vector Store & Search
    CHROMA_COLLECTION_NAME: str = "resolveai_knowledge"
    RELEVANCE_THRESHOLD: float = 0.25  # Minimum 25% relevance match

    # API Endpoint
    RESOLVEAI_API_URL: str = "http://127.0.0.1:8000"

    # Directory Paths
    DATA_DIR: Path = PROJECT_ROOT / "data"
    RAW_DIR: Path = DATA_DIR / "raw"
    EXPERT_PLAYBOOK_DIR: Path = RAW_DIR / "expert_playbooks"
    SAP_KBA_DIR: Path = RAW_DIR / "sap_kbas"
    PROCESSED_DIR: Path = DATA_DIR / "processed"
    CHROMA_DIR: Path = DATA_DIR / "chroma"

    # Processed Data Files
    CHUNKS_FILE: Path = PROCESSED_DIR / "chunks.json"
    EMBEDDED_CHUNKS_FILE: Path = PROCESSED_DIR / "embedded_chunks.json"

    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


# Global settings singleton
settings = Settings()