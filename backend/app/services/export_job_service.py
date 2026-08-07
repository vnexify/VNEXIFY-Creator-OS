from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.export_job import ExportJob
from ..repositories.export_job_repository import ExportJobRepository


class ExportJobService(BaseService[ExportJob]):
    """
    Business service encapsulating ExportJob background workflows.
    """

    def __init__(self, repository: Optional[ExportJobRepository] = None) -> None:
        self.export_job_repository = repository or ExportJobRepository()
        super().__init__(self.export_job_repository)

    def get_user_exports(self, db: Session, user_id: int) -> List[ExportJob]:
        """
        Retrieves user export jobs via repository.
        """
        return self.export_job_repository.get_by_user(db, user_id)

    def get_pending_exports(self, db: Session) -> List[ExportJob]:
        """
        Retrieves pending export jobs via repository.
        """
        return self.export_job_repository.get_pending_jobs(db)
