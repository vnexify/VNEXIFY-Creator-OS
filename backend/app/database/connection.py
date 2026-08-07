from typing import Dict, Any
from sqlalchemy import text, Engine
from sqlalchemy.exc import SQLAlchemyError
from .session import engine
from ..core.config import settings


def get_engine() -> Engine:
    """
    Returns the configured SQLAlchemy 2.x Engine instance.
    """
    return engine


def check_database_connection() -> bool:
    """
    Verifies active database engine connectivity by issuing a lightweight SQL ping.
    Returns True if database is reachable, False otherwise.
    """
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except SQLAlchemyError:
        return False
    except Exception:
        return False


def get_db_connection_info() -> Dict[str, Any]:
    """
    Returns non-sensitive metadata describing the database connection configuration.
    """
    return {
        "dialect": engine.dialect.name,
        "driver": engine.dialect.driver,
        "is_sqlite": settings.DATABASE_URL.startswith("sqlite"),
        "url_scheme": settings.DATABASE_URL.split("://")[0] if "://" in settings.DATABASE_URL else "unknown",
        "connection_healthy": check_database_connection()
    }
