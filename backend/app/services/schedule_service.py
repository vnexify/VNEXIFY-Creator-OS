from datetime import datetime
from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.schedule import Schedule
from ..repositories.schedule_repository import ScheduleRepository


class ScheduleService(BaseService[Schedule]):
    """
    Business service encapsulating Schedule publication workflows.
    """

    def __init__(self, repository: Optional[ScheduleRepository] = None) -> None:
        self.schedule_repository = repository or ScheduleRepository()
        super().__init__(self.schedule_repository)

    def get_content_schedules(self, db: Session, content_id: int) -> List[Schedule]:
        """
        Retrieves schedules for a content item via repository.
        """
        return self.schedule_repository.get_by_content(db, content_id)

    def get_pending_schedules(self, db: Session, until_time: Optional[datetime] = None) -> List[Schedule]:
        """
        Retrieves pending publication schedules via repository.
        """
        return self.schedule_repository.get_pending_schedules(db, until_time=until_time)
