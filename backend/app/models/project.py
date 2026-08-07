from typing import List, TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .workspace import Workspace
    from .folder import Folder
    from .content import Content
    from .media import Media


class Project(BaseEntity):
    """
    Project entity for organizing content campaigns and series within a workspace.
    """
    __tablename__ = "projects"

    workspace_id: Mapped[int] = mapped_column(Integer, ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    color_code: Mapped[str] = mapped_column(String(20), default="#6366F1", nullable=False)

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace", back_populates="projects")
    folders: Mapped[List["Folder"]] = relationship("Folder", back_populates="project", cascade="all, delete-orphan")
    contents: Mapped[List["Content"]] = relationship("Content", back_populates="project")
    media_assets: Mapped[List["Media"]] = relationship("Media", back_populates="project")
