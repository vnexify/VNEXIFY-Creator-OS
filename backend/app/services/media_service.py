from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.media import Media
from ..repositories.media_repository import MediaRepository


class MediaService(BaseService[Media]):
    """
    Business service encapsulating Media asset management workflows.
    """

    def __init__(self, repository: Optional[MediaRepository] = None) -> None:
        self.media_repository = repository or MediaRepository()
        super().__init__(self.media_repository)

    def get_workspace_media(self, db: Session, workspace_id: int, mime_type: Optional[str] = None) -> List[Media]:
        """
        Retrieves workspace media assets via repository.
        """
        return self.media_repository.get_by_workspace(db, workspace_id, mime_type=mime_type)

    def get_by_hash(self, db: Session, file_hash: str) -> Optional[Media]:
        """
        Retrieves media asset by file hash via repository.
        """
        return self.media_repository.get_by_hash(db, file_hash)
