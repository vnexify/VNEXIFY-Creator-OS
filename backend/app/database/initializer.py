import os
from pathlib import Path
from typing import Dict, Any
from ..core.config import settings
from .connection import check_database_connection


def ensure_db_directory() -> str:
    """
    Ensures that the directory path for the database file exists.
    Extracts file path from SQLite URL if applicable.
    """
    if settings.DATABASE_URL.startswith("sqlite:///"):
        raw_path = settings.DATABASE_URL.replace("sqlite:///", "")
        # Handle relative path resolution
        db_file_path = Path(raw_path).resolve()
        os.makedirs(db_file_path.parent, exist_ok=True)
        return str(db_file_path)
    return ""


def init_db() -> Dict[str, Any]:
    """
    Initializes database infrastructure foundation.
    Ensures storage paths exist and validates engine connectivity.
    Does NOT create tables or run migrations (deferred to Alembic).
    """
    db_path = ensure_db_directory()
    connection_ok = check_database_connection()

    return {
        "status": "initialized" if connection_ok else "degraded",
        "storage_path": db_path,
        "connection_ok": connection_ok,
        "engine_dialect": "sqlite" if settings.DATABASE_URL.startswith("sqlite") else "postgresql"
    }
