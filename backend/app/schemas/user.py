from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class UserCreate(BaseSchema):
    """
    DTO for creating a new User entity.
    """
    email: str = Field(..., description="Unique email address")
    username: str = Field(..., min_length=3, max_length=50, description="Unique username")
    full_name: Optional[str] = Field(None, max_length=100, description="User full name")
    role: str = Field("creator", description="User system role")
    is_active: bool = Field(True, description="Active status flag")


class UserUpdate(BaseSchema):
    """
    DTO for updating an existing User entity.
    """
    email: Optional[str] = Field(None, description="Updated email address")
    username: Optional[str] = Field(None, min_length=3, max_length=50, description="Updated username")
    full_name: Optional[str] = Field(None, max_length=100, description="Updated full name")
    role: Optional[str] = Field(None, description="Updated user system role")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class UserRead(TimestampSchema):
    """
    DTO for reading User entity details.
    """
    email: str = Field(..., description="Email address")
    username: str = Field(..., description="Username")
    full_name: Optional[str] = Field(None, description="Full name")
    role: str = Field(..., description="System role")


class UserResponse(SuccessResponse[UserRead]):
    """
    Response envelope DTO for single User entity payload.
    """
    pass


class UserListResponse(PaginatedResponse[UserRead]):
    """
    Response envelope DTO for paginated User entities payload.
    """
    pass
