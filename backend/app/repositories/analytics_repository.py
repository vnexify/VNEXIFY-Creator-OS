from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.analytics import Analytics


class AnalyticsRepository(BaseRepository[Analytics]):
    """
    Data-access repository for Analytics content performance metric operations.
    """

    def __init__(self) -> None:
        super().__init__(Analytics)

    def get_by_content(self, db: Session, content_id: int) -> List[Analytics]:
        """
        Retrieves all analytics records for a content item.
        """
        stmt = select(Analytics).where(Analytics.content_id == content_id).order_by(Analytics.recorded_at.desc())
        return list(db.scalars(stmt).all())

    def get_latest_metrics(self, db: Session, content_id: int) -> Optional[Analytics]:
        """
        Retrieves the most recent analytics record for a content item.
        """
        stmt = select(Analytics).where(Analytics.content_id == content_id).order_by(Analytics.recorded_at.desc()).limit(1)
        return db.scalar(stmt)
