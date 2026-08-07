from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.analytics import Analytics
from ..repositories.analytics_repository import AnalyticsRepository


class AnalyticsService(BaseService[Analytics]):
    """
    Business service encapsulating Analytics performance metric workflows.
    """

    def __init__(self, repository: Optional[AnalyticsRepository] = None) -> None:
        self.analytics_repository = repository or AnalyticsRepository()
        super().__init__(self.analytics_repository)

    def get_content_analytics(self, db: Session, content_id: int) -> List[Analytics]:
        """
        Retrieves analytics records for content via repository.
        """
        return self.analytics_repository.get_by_content(db, content_id)

    def get_latest_analytics(self, db: Session, content_id: int) -> Optional[Analytics]:
        """
        Retrieves latest analytics record for content via repository.
        """
        return self.analytics_repository.get_latest_metrics(db, content_id)
