from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.media import Media


class MediaRepository(BaseRepository[Media]):
    """
    Data-access repository for Media asset entity operations.
    """

    def __init__(self) -> None:
        super().__init__(Media)

    def get_by_workspace(self, db: Session, workspace_id: int, mime_type: Optional[str] = None) -> List[Media]:
        """
        Retrieves media assets in a workspace with optional mime-type filtering.
        """
        stmt = select(Media).where(Media.workspace_id == workspace_id)
        if mime_type:
            stmt = stmt.where(Media.mime_type.startswith(mime_type.strip()))
        return list(db.scalars(stmt.order_by(Media.created_at.desc())).all())

    def get_by_hash(self, db: Session, file_hash: str) -> Optional[Media]:
        """
        Retrieves a media asset by its unique SHA256 file hash.
        """
        stmt = select(Media).where(Media.file_hash == file_hash.strip())
        return db.scalar(stmt)
