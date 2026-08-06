from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..core.config import settings

# SQLite connection engine setup (placeholder for future migration steps)
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session() -> Generator[Session, None, None]:
    """
    Dependency generator for DB sessions.
    Placeholder initialization for Sprint 8 backend architecture.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
