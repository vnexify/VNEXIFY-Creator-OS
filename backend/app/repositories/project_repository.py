from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.project import Project


class ProjectRepository(BaseRepository[Project]):
    """
    Data-access repository for Project entity operations.
    """

    def __init__(self) -> None:
        super().__init__(Project)

    def get_by_workspace(self, db: Session, workspace_id: int) -> List[Project]:
        """
        Retrieves all projects associated with a workspace.
        """
        stmt = select(Project).where(Project.workspace_id == workspace_id)
        return list(db.scalars(stmt).all())

    def get_by_slug(self, db: Session, workspace_id: int, slug: str) -> Optional[Project]:
        """
        Retrieves a project by slug within a specific workspace.
        """
        stmt = select(Project).where(Project.workspace_id == workspace_id, Project.slug == slug.strip())
        return db.scalar(stmt)
