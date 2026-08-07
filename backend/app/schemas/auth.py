from typing import Optional
from pydantic import Field
from .base import BaseSchema, SuccessResponse
from .user import UserRead


class RegisterRequest(BaseSchema):
    """
    Registration request DTO.
    """
    email: str = Field(..., description="User email address")
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    password: str = Field(..., min_length=6, description="Plain text password")
    full_name: Optional[str] = Field(None, max_length=100, description="Optional user full name")


class LoginRequest(BaseSchema):
    """
    Login credentials request DTO.
    """
    email: str = Field(..., description="User email address")
    password: str = Field(..., description="Plain text password")


class RefreshRequest(BaseSchema):
    """
    Refresh token request DTO.
    """
    refresh_token: str = "your_refresh_token_here"


class Token(BaseSchema):
    """
    Authentication token pair DTO payload.
    """
    access_token: str = "your_access_token_here"
    refresh_token: str = "your_refresh_token_here"
    token_type: str = Field("bearer", description="Token type string")
    expires_in: int = Field(..., description="Access token expiration duration in seconds")


class TokenPayload(BaseSchema):
    """
    Decoded JWT token payload DTO.
    """
    sub: Optional[str] = Field(None, description="Subject identifier (user_id)")
    type: Optional[str] = Field(None, description="Token type (access/refresh)")
    exp: Optional[int] = Field(None, description="Expiration epoch timestamp")


class AuthResponse(SuccessResponse[Token]):
    """
    Authentication token response envelope DTO.
    """
    pass


class UserAuthResponse(SuccessResponse[UserRead]):
    """
    Current user details response envelope DTO.
    """
    pass
