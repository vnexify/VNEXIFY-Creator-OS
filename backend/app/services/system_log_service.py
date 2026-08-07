from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.system_log import SystemLog
from ..repositories.system_log_repository import SystemLogRepository


class SystemLogService(BaseService[SystemLog]):
    """
    Business service encapsulating SystemLog diagnostic logging workflows.
    """

    def __init__(self, repository: Optional[SystemLogRepository] = None) -> None:
        self.system_log_repository = repository or SystemLogRepository()
        super().__init__(self.system_log_repository)

    def get_logs_by_level(self, db: Session, level: str, limit: int = 100) -> List[SystemLog]:
        """
        Retrieves system logs filtered by severity level via repository.
        """
        return self.system_log_repository.get_by_level(db, level, limit=limit)
