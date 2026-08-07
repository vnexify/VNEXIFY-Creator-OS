from typing import List, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Integer, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity, Base

if TYPE_CHECKING:
    from .workspace import Workspace
    from .content import Content

# Junction table for Content <-> Tag many-to-many relationship
content_tags = Table(
    "content_tags",
    Base.metadata,
    Column("content_id", Integer, ForeignKey("contents.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)


class Tag(BaseEntity):
    """
    Tag entity representing granular taxonomy tags.
    """
    __tablename__ = "tags"

    workspace_id: Mapped[int] = mapped_column(Integer, ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    color_hex: Mapped[str] = mapped_column(String(20), default="#3B82F6", nullable=False)

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace", back_populates="tags")
    contents: Mapped[List["Content"]] = relationship("Content", secondary=content_tags, back_populates="tags")
