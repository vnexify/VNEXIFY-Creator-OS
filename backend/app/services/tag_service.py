from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.tag import Tag
from ..repositories.tag_repository import TagRepository


class TagService(BaseService[Tag]):
    """
    Business service encapsulating Tag taxonomy workflows.
    """

    def __init__(self, repository: Optional[TagRepository] = None) -> None:
        self.tag_repository = repository or TagRepository()
        super().__init__(self.tag_repository)

    def get_workspace_tags(self, db: Session, workspace_id: int) -> List[Tag]:
        """
        Retrieves all tags in a workspace via repository.
        """
        return self.tag_repository.get_by_workspace(db, workspace_id)

    def get_by_name(self, db: Session, workspace_id: int, name: str) -> Optional[Tag]:
        """
        Retrieves tag by name via repository.
        """
        return self.tag_repository.get_by_name(db, workspace_id, name)
