from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.project import Project
from ..repositories.project_repository import ProjectRepository


class ProjectService(BaseService[Project]):
    """
    Business service encapsulating Project management workflows.
    """

    def __init__(self, repository: Optional[ProjectRepository] = None) -> None:
        self.project_repository = repository or ProjectRepository()
        super().__init__(self.project_repository)

    def get_workspace_projects(self, db: Session, workspace_id: int) -> List[Project]:
        """
        Retrieves projects belonging to a workspace via repository.
        """
        return self.project_repository.get_by_workspace(db, workspace_id)

    def get_by_slug(self, db: Session, workspace_id: int, slug: str) -> Optional[Project]:
        """
        Retrieves project by slug in a workspace via repository.
        """
        return self.project_repository.get_by_slug(db, workspace_id, slug)
