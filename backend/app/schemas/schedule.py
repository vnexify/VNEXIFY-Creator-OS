from typing import Optional, List
from datetime import datetime
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class ScheduleCreate(BaseSchema):
    """
    DTO for creating a new Schedule entity.
    """
    content_id: int = Field(..., description="Target content item ID")
    scheduled_time: datetime = Field(..., description="Target publication UTC datetime")
    platform: str = Field(..., min_length=1, max_length=50, description="Target publication platform")
    status: str = Field("pending", description="Schedule status")
    is_active: bool = Field(True, description="Active status flag")


class ScheduleUpdate(BaseSchema):
    """
    DTO for updating an existing Schedule entity.
    """
    scheduled_time: Optional[datetime] = Field(None, description="Updated target UTC datetime")
    platform: Optional[str] = Field(None, min_length=1, max_length=50, description="Updated platform")
    status: Optional[str] = Field(None, description="Updated schedule status")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class ScheduleRead(TimestampSchema):
    """
    DTO for reading Schedule entity details.
    """
    content_id: int = Field(..., description="Target content item ID")
    scheduled_time: datetime = Field(..., description="Target publication UTC datetime")
    platform: str = Field(..., description="Publication platform")
    status: str = Field(..., description="Schedule status")


class ScheduleResponse(SuccessResponse[ScheduleRead]):
    """
    Response envelope DTO for single Schedule entity payload.
    """
    pass


class ScheduleListResponse(PaginatedResponse[ScheduleRead]):
    """
    Response envelope DTO for paginated Schedule entities payload.
    """
    pass
