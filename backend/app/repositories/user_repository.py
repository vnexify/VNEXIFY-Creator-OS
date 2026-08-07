from typing import Optional
from sqlalchemy import select
from sqlalchemy.orm import Session
from .base_repository import BaseRepository
from ..models.user import User


class UserRepository(BaseRepository[User]):
    """
    Data-access repository for User entity operations.
    """

    def __init__(self) -> None:
        super().__init__(User)

    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """
        Retrieves a user by their unique email address.
        """
        stmt = select(User).where(User.email == email.lower().strip())
        return db.scalar(stmt)

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        """
        Retrieves a user by their unique username.
        """
        stmt = select(User).where(User.username == username.strip())
        return db.scalar(stmt)
