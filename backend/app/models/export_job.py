from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .user import User


class ExportJob(BaseEntity):
    """
    ExportJob entity representing background content or workspace export processes.
    """
    __tablename__ = "export_jobs"

    user_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)

    export_type: Mapped[str] = mapped_column(String(50), nullable=False, index=True)  # e.g., json, markdown, zip
    status: Mapped[str] = mapped_column(String(50), default="pending", nullable=False, index=True)
    file_path: Mapped[Optional[str]] = mapped_column(String(512), nullable=True)
    error_message: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relationships
    user: Mapped[Optional["User"]] = relationship("User", back_populates="export_jobs")
