from typing import Optional
from sqlalchemy.orm import Session
from .base_service import BaseService
from ..models.user import User
from ..repositories.user_repository import UserRepository


class UserService(BaseService[User]):
    """
    Business service encapsulating User management workflows.
    """

    def __init__(self, repository: Optional[UserRepository] = None) -> None:
        self.user_repository = repository or UserRepository()
        super().__init__(self.user_repository)

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """
        Retrieves user by email address via repository.
        """
        return self.user_repository.get_by_email(db, email)

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        """
        Retrieves user by username via repository.
        """
        return self.user_repository.get_by_username(db, username)
