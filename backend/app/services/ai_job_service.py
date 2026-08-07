from typing import Optional, List
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.ai_job import AIJob
from ..repositories.ai_job_repository import AIJobRepository


class AIJobService(BaseService[AIJob]):
    """
    Business service encapsulating AIJob generation log workflows.
    """

    def __init__(self, repository: Optional[AIJobRepository] = None) -> None:
        self.ai_job_repository = repository or AIJobRepository()
        super().__init__(self.ai_job_repository)

    def get_user_jobs(self, db: Session, user_id: int) -> List[AIJob]:
        """
        Retrieves user AI jobs via repository.
        """
        return self.ai_job_repository.get_by_user(db, user_id)

    def get_provider_jobs(self, db: Session, provider_id: int) -> List[AIJob]:
        """
        Retrieves provider AI jobs via repository.
        """
        return self.ai_job_repository.get_by_provider(db, provider_id)
