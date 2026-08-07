from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.workspace import Workspace


class WorkspaceRepository(BaseRepository[Workspace]):
    """
    Data-access repository for Workspace entity operations.
    """

    def __init__(self) -> None:
        super().__init__(Workspace)

    def get_by_slug(self, db: Session, slug: str) -> Optional[Workspace]:
        """
        Retrieves a workspace by its unique slug identifier.
        """
        stmt = select(Workspace).where(Workspace.slug == slug.strip())
        return db.scalar(stmt)

    def get_by_owner(self, db: Session, owner_id: int) -> List[Workspace]:
        """
        Retrieves all workspaces owned by a specific user.
        """
        stmt = select(Workspace).where(Workspace.owner_id == owner_id)
        return list(db.scalars(stmt).all())
