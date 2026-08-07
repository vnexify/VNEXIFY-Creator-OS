from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .user import User
    from .ai_provider import AIProvider


class AIJob(BaseEntity):
    """
    AIJob entity recording AI generation requests, tokens used, and performance metrics.
    """
    __tablename__ = "ai_jobs"

    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
    provider_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("ai_providers.id", ondelete="SET NULL"), nullable=True, index=True)

    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    response: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="completed", nullable=False, index=True)
    tokens_used: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    duration_ms: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Relationships
    user: Mapped[Optional["User"]] = relationship("User", back_populates="ai_jobs")
    provider: Mapped[Optional["AIProvider"]] = relationship("AIProvider", back_populates="jobs")
