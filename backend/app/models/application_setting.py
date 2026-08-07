from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .workspace import Workspace


class ApplicationSetting(BaseEntity):
    """
    ApplicationSetting entity managing key-value configuration options.
    """
    __tablename__ = "application_settings"

    workspace_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=True, index=True)

    key: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    value: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    setting_type: Mapped[str] = mapped_column(String(50), default="string", nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    # Relationships
    workspace: Mapped[Optional["Workspace"]] = relationship("Workspace", back_populates="settings")
