from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.content import Content


class ContentRepository(BaseRepository[Content]):
    """
    Data-access repository for Content entity operations.
    """

    def __init__(self) -> None:
        super().__init__(Content)

    def get_by_workspace(self, db: Session, workspace_id: int, status: Optional[str] = None) -> List[Content]:
        """
        Retrieves content items in a workspace with optional status filtering.
        """
        stmt = select(Content).where(Content.workspace_id == workspace_id)
        if status:
            stmt = stmt.where(Content.status == status.strip())
        return list(db.scalars(stmt.order_by(Content.updated_at.desc())).all())

    def get_by_slug(self, db: Session, workspace_id: int, slug: str) -> Optional[Content]:
        """
        Retrieves a content item by slug within a workspace.
        """
        stmt = select(Content).where(Content.workspace_id == workspace_id, Content.slug == slug.strip())
        return db.scalar(stmt)

    def get_by_project(self, db: Session, project_id: int) -> List[Content]:
        """
        Retrieves all content items belonging to a project.
        """
        stmt = select(Content).where(Content.project_id == project_id)
        return list(db.scalars(stmt.order_by(Content.updated_at.desc())).all())
