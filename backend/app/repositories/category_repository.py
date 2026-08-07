from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.category import Category


class CategoryRepository(BaseRepository[Category]):
    """
    Data-access repository for Category entity operations.
    """

    def __init__(self) -> None:
        super().__init__(Category)

    def get_by_workspace(self, db: Session, workspace_id: int) -> List[Category]:
        """
        Retrieves all categories within a workspace.
        """
        stmt = select(Category).where(Category.workspace_id == workspace_id)
        return list(db.scalars(stmt).all())

    def get_by_slug(self, db: Session, workspace_id: int, slug: str) -> Optional[Category]:
        """
        Retrieves a category by slug in a workspace.
        """
        stmt = select(Category).where(Category.workspace_id == workspace_id, Category.slug == slug.strip())
        return db.scalar(stmt)
