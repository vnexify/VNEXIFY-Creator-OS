from datetime import datetime, timezone
from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .content import Content


class Analytics(BaseEntity):
    """
    Analytics entity storing performance metrics (views, likes, shares) for content.
    """
    __tablename__ = "analytics"

    content_id: Mapped[int] = mapped_column(Integer, ForeignKey("contents.id", ondelete="CASCADE"), nullable=False, index=True)

    views_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    likes_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    shares_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    comments_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    recorded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
        index=True
    )

    # Relationships
    content: Mapped["Content"] = relationship("Content", back_populates="analytics_records")
