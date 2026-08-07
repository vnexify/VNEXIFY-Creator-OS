from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, ForeignKey, Integer, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .workspace import Workspace
    from .project import Project
    from .folder import Folder
    from .content import Content


class Media(BaseEntity):
    """
    Media entity representing local asset files (images, audio, video, thumbnails).
    """
    __tablename__ = "media_assets"

    workspace_id: Mapped[int] = mapped_column(Integer, ForeignKey("workspaces.id", ondelete="CASCADE"), nullable=False, index=True)
    project_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("projects.id", ondelete="SET NULL"), nullable=True, index=True)
    folder_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("folders.id", ondelete="SET NULL"), nullable=True, index=True)
    content_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("contents.id", ondelete="SET NULL"), nullable=True, index=True)

    file_name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    file_path: Mapped[str] = mapped_column(String(512), nullable=False)
    file_hash: Mapped[Optional[str]] = mapped_column(String(64), nullable=True, index=True)
    mime_type: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    file_size_bytes: Mapped[int] = mapped_column(BigInteger, default=0, nullable=False)

    # Relationships
    workspace: Mapped["Workspace"] = relationship("Workspace", back_populates="media_assets")
    project: Mapped[Optional["Project"]] = relationship("Project", back_populates="media_assets")
    folder: Mapped[Optional["Folder"]] = relationship("Folder", back_populates="media_assets")
    content: Mapped[Optional["Content"]] = relationship("Content", back_populates="media_assets")
