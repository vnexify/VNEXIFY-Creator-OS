from typing import Optional
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.ai_provider import AIProvider
from ..repositories.ai_provider_repository import AIProviderRepository


class AIProviderService(BaseService[AIProvider]):
    """
    Business service encapsulating AIProvider configuration workflows.
    """

    def __init__(self, repository: Optional[AIProviderRepository] = None) -> None:
        self.ai_provider_repository = repository or AIProviderRepository()
        super().__init__(self.ai_provider_repository)

    def get_by_name(self, db: Session, name: str) -> Optional[AIProvider]:
        """
        Retrieves AI provider by name via repository.
        """
        return self.ai_provider_repository.get_by_name(db, name)

    def get_default_provider(self, db: Session) -> Optional[AIProvider]:
        """
        Retrieves default configured AI provider via repository.
        """
        return self.ai_provider_repository.get_default_provider(db)
