from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.ai_provider import AIProvider


class AIProviderRepository(BaseRepository[AIProvider]):
    """
    Data-access repository for AIProvider entity operations.
    """

    def __init__(self) -> None:
        super().__init__(AIProvider)

    def get_by_name(self, db: Session, name: str) -> Optional[AIProvider]:
        """
        Retrieves an AI provider by name.
        """
        stmt = select(AIProvider).where(AIProvider.name == name.strip())
        return db.scalar(stmt)

    def get_default_provider(self, db: Session) -> Optional[AIProvider]:
        """
        Retrieves the default configured AI provider.
        """
        stmt = select(AIProvider).where(AIProvider.is_default.is_(True))
        return db.scalar(stmt)
