from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.folder import Folder


class FolderRepository(BaseRepository[Folder]):
    """
    Data-access repository for Folder hierarchical tree operations.
    """

    def __init__(self) -> None:
        super().__init__(Folder)

    def get_by_workspace(self, db: Session, workspace_id: int) -> List[Folder]:
        """
        Retrieves all folders in a workspace.
        """
        stmt = select(Folder).where(Folder.workspace_id == workspace_id)
        return list(db.scalars(stmt).all())

    def get_root_folders(self, db: Session, workspace_id: int) -> List[Folder]:
        """
        Retrieves root folders (parent_id IS NULL) in a workspace.
        """
        stmt = select(Folder).where(Folder.workspace_id == workspace_id, Folder.parent_id.is_(None))
        return list(db.scalars(stmt).all())

    def get_children(self, db: Session, parent_id: int) -> List[Folder]:
        """
        Retrieves immediate sub-folders for a parent folder ID.
        """
        stmt = select(Folder).where(Folder.parent_id == parent_id)
        return list(db.scalars(stmt).all())
