from typing import List, TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import BaseEntity

if TYPE_CHECKING:
    from .workspace import Workspace
    from .content import Content
    from .ai_job import AIJob
    from .export_job import ExportJob
    from .notification import Notification


class User(BaseEntity):
    """
    User entity representing system creators and workspace owners.
    """
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=True)
    avatar_url: Mapped[str] = mapped_column(String(512), nullable=True)
    role: Mapped[str] = mapped_column(String(50), default="creator", nullable=False)

    # Relationships
    owned_workspaces: Mapped[List["Workspace"]] = relationship("Workspace", back_populates="owner", cascade="all, delete-orphan")
    contents: Mapped[List["Content"]] = relationship("Content", back_populates="author")
    ai_jobs: Mapped[List["AIJob"]] = relationship("AIJob", back_populates="user", cascade="all, delete-orphan")
    export_jobs: Mapped[List["ExportJob"]] = relationship("ExportJob", back_populates="user", cascade="all, delete-orphan")
    notifications: Mapped[List["Notification"]] = relationship("Notification", back_populates="user", cascade="all, delete-orphan")
