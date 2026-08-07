from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.workspace import Workspace
from ..repositories.workspace_repository import WorkspaceRepository


class WorkspaceService(BaseService[Workspace]):
    """
    Business service encapsulating Workspace management workflows.
    """

    def __init__(self, repository: Optional[WorkspaceRepository] = None) -> None:
        self.workspace_repository = repository or WorkspaceRepository()
        super().__init__(self.workspace_repository)

    def get_by_slug(self, db: Session, slug: str) -> Optional[Workspace]:
        """
        Retrieves workspace by slug via repository.
        """
        return self.workspace_repository.get_by_slug(db, slug)

    def get_user_workspaces(self, db: Session, owner_id: int) -> List[Workspace]:
        """
        Retrieves all workspaces owned by a user via repository.
        """
        return self.workspace_repository.get_by_owner(db, owner_id)
