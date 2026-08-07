from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .content import Content


class Schedule(BaseEntity):
    """
    Schedule entity representing publication timing and social platform deployment slots.
    """
    __tablename__ = "schedules"

    content_id: Mapped[int] = mapped_column(Integer, ForeignKey("contents.id", ondelete="CASCADE"), nullable=False, index=True)
    scheduled_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, index=True)
    platform: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    status: Mapped[str] = mapped_column(String(50), default="pending", nullable=False, index=True)
    publish_url: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)

    # Relationships
    content: Mapped["Content"] = relationship("Content", back_populates="schedules")
