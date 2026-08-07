from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.application_setting import ApplicationSetting


class ApplicationSettingRepository(BaseRepository[ApplicationSetting]):
    """
    Data-access repository for ApplicationSetting key-value operations.
    """

    def __init__(self) -> None:
        super().__init__(ApplicationSetting)

    def get_by_key(self, db: Session, key: str) -> Optional[ApplicationSetting]:
        """
        Retrieves a global setting by its key.
        """
        stmt = select(ApplicationSetting).where(ApplicationSetting.key == key.strip())
        return db.scalar(stmt)

    def get_by_workspace(self, db: Session, workspace_id: int) -> List[ApplicationSetting]:
        """
        Retrieves setting entries associated with a workspace.
        """
        stmt = select(ApplicationSetting).where(ApplicationSetting.workspace_id == workspace_id)
        return list(db.scalars(stmt).all())
