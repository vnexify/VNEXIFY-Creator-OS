from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.ai_job import AIJob


class AIJobRepository(BaseRepository[AIJob]):
    """
    Data-access repository for AIJob execution log entity operations.
    """

    def __init__(self) -> None:
        super().__init__(AIJob)

    def get_by_user(self, db: Session, user_id: int) -> List[AIJob]:
        """
        Retrieves all AI jobs performed by a user.
        """
        stmt = select(AIJob).where(AIJob.user_id == user_id).order_by(AIJob.created_at.desc())
        return list(db.scalars(stmt).all())

    def get_by_provider(self, db: Session, provider_id: int) -> List[AIJob]:
        """
        Retrieves all AI jobs executed using a specific provider.
        """
        stmt = select(AIJob).where(AIJob.provider_id == provider_id).order_by(AIJob.created_at.desc())
        return list(db.scalars(stmt).all())
