from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.application_setting import ApplicationSetting
from ..repositories.application_setting_repository import ApplicationSettingRepository


class ApplicationSettingService(BaseService[ApplicationSetting]):
    """
    Business service encapsulating ApplicationSetting workflows.
    """

    def __init__(self, repository: Optional[ApplicationSettingRepository] = None) -> None:
        self.setting_repository = repository or ApplicationSettingRepository()
        super().__init__(self.setting_repository)

    def get_setting_by_key(self, db: Session, key: str) -> Optional[ApplicationSetting]:
        """
        Retrieves setting entry by key via repository.
        """
        return self.setting_repository.get_by_key(db, key)

    def get_workspace_settings(self, db: Session, workspace_id: int) -> List[ApplicationSetting]:
        """
        Retrieves setting entries for a workspace via repository.
        """
        return self.setting_repository.get_by_workspace(db, workspace_id)
