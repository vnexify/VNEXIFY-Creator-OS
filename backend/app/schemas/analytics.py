from typing import Optional, List
from datetime import datetime
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class AnalyticsCreate(BaseSchema):
    """
    DTO for creating a new Analytics content performance record.
    """
    views: int = Field(0, ge=0, description="Total view count")
    clicks: int = Field(0, ge=0, description="Total click count")
    shares: int = Field(0, ge=0, description="Total share count")
    engagement_rate: float = Field(0.0, ge=0.0, description="Engagement rate percentage")
    content_id: int = Field(..., description="Target content item ID")
    recorded_at: datetime = Field(..., description="Record UTC timestamp")
    is_active: bool = Field(True, description="Active status flag")


class AnalyticsUpdate(BaseSchema):
    """
    DTO for updating an existing Analytics content performance record.
    """
    views: Optional[int] = Field(None, ge=0, description="Updated view count")
    clicks: Optional[int] = Field(None, ge=0, description="Updated click count")
    shares: Optional[int] = Field(None, ge=0, description="Updated share count")
    engagement_rate: Optional[float] = Field(None, ge=0.0, description="Updated engagement rate")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class AnalyticsRead(TimestampSchema):
    """
    DTO for reading Analytics content performance details.
    """
    views: int = Field(..., description="View count")
    clicks: int = Field(..., description="Click count")
    shares: int = Field(..., description="Share count")
    engagement_rate: float = Field(..., description="Engagement rate percentage")
    content_id: int = Field(..., description="Target content item ID")
    recorded_at: datetime = Field(..., description="Record UTC timestamp")


class AnalyticsResponse(SuccessResponse[AnalyticsRead]):
    """
    Response envelope DTO for single Analytics entity payload.
    """
    pass


class AnalyticsListResponse(PaginatedResponse[AnalyticsRead]):
    """
    Response envelope DTO for paginated Analytics entities payload.
    """
    pass
