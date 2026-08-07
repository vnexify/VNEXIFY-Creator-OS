from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.tag import Tag


class TagRepository(BaseRepository[Tag]):
    """
    Data-access repository for Tag entity operations.
    """

    def __init__(self) -> None:
        super().__init__(Tag)

    def get_by_workspace(self, db: Session, workspace_id: int) -> List[Tag]:
        """
        Retrieves all taxonomy tags in a workspace.
        """
        stmt = select(Tag).where(Tag.workspace_id == workspace_id)
        return list(db.scalars(stmt).all())

    def get_by_name(self, db: Session, workspace_id: int, name: str) -> Optional[Tag]:
        """
        Retrieves a tag by name in a workspace.
        """
        stmt = select(Tag).where(Tag.workspace_id == workspace_id, Tag.name == name.strip())
        return db.scalar(stmt)
