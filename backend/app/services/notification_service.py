from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.notification import Notification
from ..repositories.notification_repository import NotificationRepository


class NotificationService(BaseService[Notification]):
    """
    Business service encapsulating Notification workflows.
    """

    def __init__(self, repository: Optional[NotificationRepository] = None) -> None:
        self.notification_repository = repository or NotificationRepository()
        super().__init__(self.notification_repository)

    def get_user_notifications(self, db: Session, user_id: int, unread_only: bool = False) -> List[Notification]:
        """
        Retrieves user notifications via repository.
        """
        return self.notification_repository.get_by_user(db, user_id, unread_only=unread_only)
