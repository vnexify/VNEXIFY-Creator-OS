from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .ai_job import AIJob


class AIProvider(BaseEntity):
    """
    AIProvider entity representing configured local or cloud AI models and endpoints.
    """
    __tablename__ = "ai_providers"

    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    provider_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)  # e.g., Ollama, OpenAI, Gemini
    api_base_url: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    # Relationships
    jobs: Mapped[List["AIJob"]] = relationship("AIJob", back_populates="provider", cascade="all, delete-orphan")
