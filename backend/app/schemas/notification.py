from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class NotificationCreate(BaseSchema):
    """
    DTO for creating a new Notification entity.
    """
    title: str = Field(..., min_length=1, max_length=200, description="Notification title")
    message: str = Field(..., min_length=1, description="Notification body text")
    type: str = Field("info", description="Notification type category")
    is_read: bool = Field(False, description="Read status flag")
    user_id: int = Field(..., description="Target user ID")
    is_active: bool = Field(True, description="Active status flag")


class NotificationUpdate(BaseSchema):
    """
    DTO for updating an existing Notification entity.
    """
    title: Optional[str] = Field(None, min_length=1, max_length=200, description="Updated title")
    message: Optional[str] = Field(None, description="Updated message body")
    type: Optional[str] = Field(None, description="Updated type category")
    is_read: Optional[bool] = Field(None, description="Updated read status flag")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class NotificationRead(TimestampSchema):
    """
    DTO for reading Notification entity details.
    """
    title: str = Field(..., description="Notification title")
    message: str = Field(..., description="Message body text")
    type: str = Field(..., description="Type category")
    is_read: bool = Field(..., description="Read status flag")
    user_id: int = Field(..., description="Target user ID")


class NotificationResponse(SuccessResponse[NotificationRead]):
    """
    Response envelope DTO for single Notification entity payload.
    """
    pass


class NotificationListResponse(PaginatedResponse[NotificationRead]):
    """
    Response envelope DTO for paginated Notification entities payload.
    """
    pass
