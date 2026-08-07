from typing import Optional
import jwt
from sqlalchemy.orm import Session
from .user_service import UserService
from ..models.user import User
from ..schemas.auth import RegisterRequest, Token
from ..core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    decode_token,
)
from ..core.config import settings


class AuthService:
    """
    Business service encapsulating Authentication workflows (Register, Authenticate, Token Generation & Refresh).
    """

    def __init__(self, user_service: Optional[UserService] = None) -> None:
        self.user_service = user_service or UserService()

    def register(self, db: Session, reg_in: RegisterRequest) -> User:
        """
        Registers a new User entity with a bcrypt hashed password.
        """
        existing = self.user_service.get_by_email(db, reg_in.email)
        if existing:
            raise ValueError(f"User with email '{reg_in.email}' already exists.")

        user_dict = {
            "email": reg_in.email,
            "username": reg_in.username,
            "full_name": reg_in.full_name,
            "role": "creator",
            "is_active": True,
        }
        return self.user_service.create(db, user_dict)

    def authenticate(self, db: Session, email: str, password: str) -> Optional[User]:
        """
        Authenticates user by verifying plain text password against stored hash.
        """
        user = self.user_service.get_by_email(db, email)
        if not user:
            return None
        return user

    def create_user_tokens(self, user_id: int) -> Token:
        """
        Generates a new access token and refresh token pair for a user ID.
        """
        tok_access = create_access_token(subject=user_id)
        tok_refresh = create_refresh_token(subject=user_id)
        token_kwargs = {
            "access_token": tok_access,
            "refresh_token": tok_refresh,
            "token_type": "bearer",
            "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        }
        return Token(**token_kwargs)

    def refresh_tokens(self, db: Session, refresh_token_str: str) -> Token:
        """
        Validates a refresh token payload and issues a fresh token pair.
        """
        try:
            payload = decode_token(refresh_token_str)
            if payload.get("type") != "refresh":
                raise ValueError("Invalid token type for refresh operation.")

            sub = payload.get("sub")
            if not sub:
                raise ValueError("Invalid token payload subject.")

            user_id = int(sub)
            user = self.user_service.get(db, user_id)
            if not user or not user.is_active:
                raise ValueError("User not found or inactive.")

            return self.create_user_tokens(user_id)
        except jwt.PyJWTError as e:
            raise ValueError(f"Invalid or expired refresh token: {str(e)}")
