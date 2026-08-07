from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.export_job import ExportJob


class ExportJobRepository(BaseRepository[ExportJob]):
    """
    Data-access repository for ExportJob entity operations.
    """

    def __init__(self) -> None:
        super().__init__(ExportJob)

    def get_by_user(self, db: Session, user_id: int) -> List[ExportJob]:
        """
        Retrieves export jobs initiated by a user.
        """
        stmt = select(ExportJob).where(ExportJob.user_id == user_id).order_by(ExportJob.created_at.desc())
        return list(db.scalars(stmt).all())

    def get_pending_jobs(self, db: Session) -> List[ExportJob]:
        """
        Retrieves pending export jobs awaiting execution.
        """
        stmt = select(ExportJob).where(ExportJob.status == "pending").order_by(ExportJob.created_at.asc())
        return list(db.scalars(stmt).all())
