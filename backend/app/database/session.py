from typing import Generator, ContextManager
from contextlib import contextmanager
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from ..core.config import settings

# Configure SQLAlchemy 2.x Database Engine
engine_kwargs = {
    "echo": False,
    "pool_pre_ping": True,
}

if settings.DATABASE_URL.startswith("sqlite"):
    engine_kwargs["connect_args"] = {"check_same_thread": False}

engine: Engine = create_engine(
    settings.DATABASE_URL,
    **engine_kwargs
)

# Configure SQLAlchemy Session Factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)


class DatabaseSessionManager:
    """
    Context manager for database sessions providing explicit session lifespan management
    for background tasks, CLI commands, and service layer operations.
    """
    def __init__(self) -> None:
        self.session_factory = SessionLocal

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        session: Session = self.session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


def get_db_session() -> Generator[Session, None, None]:
    """
    FastAPI dependency generator providing request-scoped database sessions.
    Automatically handles rollback on exceptions and cleanup upon request completion.
    """
    session: Session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
