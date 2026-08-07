from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.system_log import SystemLog


class SystemLogRepository(BaseRepository[SystemLog]):
    """
    Data-access repository for SystemLog diagnostic record operations.
    """

    def __init__(self) -> None:
        super().__init__(SystemLog)

    def get_by_level(self, db: Session, level: str, limit: int = 100) -> List[SystemLog]:
        """
        Retrieves recent system log records filtered by severity level.
        """
        stmt = select(SystemLog).where(SystemLog.level == level.upper().strip()).order_by(SystemLog.created_at.desc()).limit(limit)
        return list(db.scalars(stmt).all())
