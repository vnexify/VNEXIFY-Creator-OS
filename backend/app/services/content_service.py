from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.content import Content
from ..repositories.content_repository import ContentRepository


class ContentService(BaseService[Content]):
    """
    Business service encapsulating Content creation, publishing, and draft workflows.
    """

    def __init__(self, repository: Optional[ContentRepository] = None) -> None:
        self.content_repository = repository or ContentRepository()
        super().__init__(self.content_repository)

    def get_workspace_content(self, db: Session, workspace_id: int, status: Optional[str] = None) -> List[Content]:
        """
        Retrieves workspace content items via repository.
        """
        return self.content_repository.get_by_workspace(db, workspace_id, status=status)

    def get_by_slug(self, db: Session, workspace_id: int, slug: str) -> Optional[Content]:
        """
        Retrieves content item by slug via repository.
        """
        return self.content_repository.get_by_slug(db, workspace_id, slug)

    def get_project_content(self, db: Session, project_id: int) -> List[Content]:
        """
        Retrieves content items for a project via repository.
        """
        return self.content_repository.get_by_project(db, project_id)
