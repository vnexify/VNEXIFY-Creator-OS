from datetime import datetime, timezone
import uuid
from sqlalchemy import Integer, String, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    Root declarative base class for all SQLAlchemy ORM models.
    """
    pass


class BaseEntity(Base):
    """
    Abstract base entity class providing standardized columns across all models:
    - id (Integer primary key)
    - uuid (String 36 unique identifier)
    - is_active (Boolean status flag)
    - created_at (UTC Timestamp)
    - updated_at (UTC Timestamp with auto-update)
    """
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[str] = mapped_column(
        String(36),
        unique=True,
        nullable=False,
        index=True,
        default=lambda: str(uuid.uuid4())
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )
