from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .workspace import Workspace
    from .project import Project
    from .content import Content
    from .media import Media


class Folder(BaseEntity):
    """
    Folder entity representing hierarchical asset and content organizational trees.
    """
    __tablename__ = "folders"

    workspace_id: Mapped[int] = mapped_column(Integer, ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False, index=True)
    project_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("projects.id", ondelete="SET NULL"), nullable=True, index=True)
    parent_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("folders.id", ondelete="CASCADE"), nullable=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace", back_populates="folders")
    project: Mapped[Optional["Project"]] = relationship("Project", back_populates="folders")
    parent: Mapped[Optional["Folder"]] = relationship("Folder", remote_side="Folder.id", back_populates="children")
    children: Mapped[List["Folder"]] = relationship("Folder", back_populates="parent", cascade="all, delete-orphan")
    contents: Mapped[List["Content"]] = relationship("Content", back_populates="folder")
    media_assets: Mapped[List["Media"]] = relationship("Media", back_populates="folder")
