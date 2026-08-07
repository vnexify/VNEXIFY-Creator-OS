from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.notification import Notification


class NotificationRepository(BaseRepository[Notification]):
    """
    Data-access repository for Notification entity operations.
    """

    def __init__(self) -> None:
        super().__init__(Notification)

    def get_by_user(self, db: Session, user_id: int, unread_only: bool = False) -> List[Notification]:
        """
        Retrieves user notifications with optional unread status filtering.
        """
        stmt = select(Notification).where(Notification.user_id == user_id)
        if unread_only:
            stmt = stmt.where(Notification.is_read.is_(False))
        return list(db.scalars(stmt.order_by(Notification.created_at.desc())).all())
