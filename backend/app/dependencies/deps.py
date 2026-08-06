from typing import Generator
from sqlalchemy.orm import Session
from ..database.session import get_db_session
from ..core.config import settings, Settings


def get_db() -> Generator[Session, None, None]:
    """
    FastAPI dependency wrapper for obtaining database sessions.
    """
    yield from get_db_session()


def get_app_settings() -> Settings:
    """
    FastAPI dependency for accessing application settings.
    """
    return settings
