from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity
from .tag import content_tags

if TYPE_CHECKING:
    from .workspace import Workspace
    from .project import Project
    from .folder import Folder
    from .category import Category
    from .user import User
    from .tag import Tag
    from .media import Media
    from .schedule import Schedule
    from .analytics import Analytics


class Content(BaseEntity):
    """
    Content entity representing core creator drafts, articles, scripts, and video posts.
    """
    __tablename__ = "contents"

    workspace_id: Mapped[int] = mapped_column(Integer, ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False, index=True)
    project_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("projects.id", ondelete="SET NULL"), nullable=True, index=True)
    folder_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("folders.id", ondelete="SET NULL"), nullable=True, index=True)
    category_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True, index=True)
    author_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)

    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    slug: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    body: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    excerpt: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="draft", nullable=False, index=True)
    word_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace", back_populates="contents")
    project: Mapped[Optional["Project"]] = relationship("Project", back_populates="contents")
    folder: Mapped[Optional["Folder"]] = relationship("Folder", back_populates="contents")
    category: Mapped[Optional["Category"]] = relationship("Category", back_populates="contents")
    author: Mapped[Optional["User"]] = relationship("User", back_populates="contents")
    tags: Mapped[List["Tag"]] = relationship("Tag", secondary=content_tags, back_populates="contents")
    media_assets: Mapped[List["Media"]] = relationship("Media", back_populates="content")
    schedules: Mapped[List["Schedule"]] = relationship("Schedule", back_populates="content", cascade="all, delete-orphan")
    analytics_records: Mapped[List["Analytics"]] = relationship("Analytics", back_populates="content", cascade="all, delete-orphan")
