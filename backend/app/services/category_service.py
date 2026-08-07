from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.category import Category
from ..repositories.category_repository import CategoryRepository


class CategoryService(BaseService[Category]):
    """
    Business service encapsulating Category management workflows.
    """

    def __init__(self, repository: Optional[CategoryRepository] = None) -> None:
        self.category_repository = repository or CategoryRepository()
        super().__init__(self.category_repository)

    def get_workspace_categories(self, db: Session, workspace_id: int) -> List[Category]:
        """
        Retrieves all categories in a workspace via repository.
        """
        return self.category_repository.get_by_workspace(db, workspace_id)

    def get_by_slug(self, db: Session, workspace_id: int, slug: str) -> Optional[Category]:
        """
        Retrieves category by slug via repository.
        """
        return self.category_repository.get_by_slug(db, workspace_id, slug)
