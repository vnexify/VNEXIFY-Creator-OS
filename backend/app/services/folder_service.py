from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.folder import Folder
from ..repositories.folder_repository import FolderRepository


class FolderService(BaseService[Folder]):
    """
    Business service encapsulating Folder tree organizational workflows.
    """

    def __init__(self, repository: Optional[FolderRepository] = None) -> None:
        self.folder_repository = repository or FolderRepository()
        super().__init__(self.folder_repository)

    def get_workspace_folders(self, db: Session, workspace_id: int) -> List[Folder]:
        """
        Retrieves all folders in a workspace via repository.
        """
        return self.folder_repository.get_by_workspace(db, workspace_id)

    def get_root_folders(self, db: Session, workspace_id: int) -> List[Folder]:
        """
        Retrieves root folders in a workspace via repository.
        """
        return self.folder_repository.get_root_folders(db, workspace_id)

    def get_subfolders(self, db: Session, parent_id: int) -> List[Folder]:
        """
        Retrieves child sub-folders via repository.
        """
        return self.folder_repository.get_children(db, parent_id)
