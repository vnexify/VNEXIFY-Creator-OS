from datetime import datetime
from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.schedule import Schedule


class ScheduleRepository(BaseRepository[Schedule]):
    """
    Data-access repository for Schedule entity operations.
    """

    def __init__(self) -> None:
        super().__init__(Schedule)

    def get_by_content(self, db: Session, content_id: int) -> List[Schedule]:
        """
        Retrieves all schedules attached to a specific content item.
        """
        stmt = select(Schedule).where(Schedule.content_id == content_id)
        return list(db.scalars(stmt).all())

    def get_pending_schedules(self, db: Session, until_time: Optional[datetime] = None) -> List[Schedule]:
        """
        Retrieves pending schedules due for publication up to an optional timestamp.
        """
        stmt = select(Schedule).where(Schedule.status == "pending")
        if until_time:
            stmt = stmt.where(Schedule.scheduled_time <= until_time)
        return list(db.scalars(stmt.order_by(Schedule.scheduled_time.asc())).all())
