from typing import List, TYPE_CHECKING
from sqlalchemy import String, Text, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .user import User
    from .project import Project
    from .folder import Folder
    from .category import Category
    from .tag import Tag
    from .content import Content
    from .media import Media
    from .application_setting import ApplicationSetting


class Workspace(BaseEntity):
    """
    Workspace entity representing isolated content creation environments.
    """
    __tablename__ = "workspaces"

    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    # Relationships
    owner: Mapped["User"] = relationship("User", back_populates="owned_workspaces")
    projects: Mapped[List["Project"]] = relationship("Project", back_populates="workspace", cascade="all, delete-orphan")
    folders: Mapped[List["Folder"]] = relationship("Folder", back_populates="workspace", cascade="all, delete-orphan")
    categories: Mapped[List["Category"]] = relationship("Category", back_populates="workspace", cascade="all, delete-orphan")
    tags: Mapped[List["Tag"]] = relationship("Tag", back_populates="workspace", cascade="all, delete-orphan")
    contents: Mapped[List["Content"]] = relationship("Content", back_populates="workspace", cascade="all, delete-orphan")
    media_assets: Mapped[List["Media"]] = relationship("Media", back_populates="workspace", cascade="all, delete-orphan")
    settings: Mapped[List["ApplicationSetting"]] = relationship("ApplicationSetting", back_populates="workspace", cascade="all, delete-orphan")
