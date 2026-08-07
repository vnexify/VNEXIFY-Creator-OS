from typing import List, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .workspace import Workspace
    from .content import Content


class Category(BaseEntity):
    """
    Category entity representing primary content classifications.
    """
    __tablename__ = "categories"

    workspace_id: Mapped[int] = mapped_column(Integer, ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    color_code: Mapped[str] = mapped_column(String(20), default="#10B981", nullable=False)

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace", back_populates="categories")
    contents: Mapped[List["Content"]] = relationship("Content", back_populates="category")
