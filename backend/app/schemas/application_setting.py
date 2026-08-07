from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class ApplicationSettingCreate(BaseSchema):
    """
    DTO for creating a new ApplicationSetting entity.
    """
    key: str = Field(..., min_length=1, max_length=100, description="Unique setting key")
    value: Optional[str] = Field(None, description="Setting value string")
    workspace_id: Optional[int] = Field(None, description="Optional workspace scope ID")
    is_active: bool = Field(True, description="Active status flag")


class ApplicationSettingUpdate(BaseSchema):
    """
    DTO for updating an existing ApplicationSetting entity.
    """
    value: Optional[str] = Field(None, description="Updated setting value")
    workspace_id: Optional[int] = Field(None, description="Updated workspace scope ID")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class ApplicationSettingRead(TimestampSchema):
    """
    DTO for reading ApplicationSetting entity details.
    """
    key: str = Field(..., description="Setting key")
    value: Optional[str] = Field(None, description="Setting value")
    workspace_id: Optional[int] = Field(None, description="Workspace scope ID")


class ApplicationSettingResponse(SuccessResponse[ApplicationSettingRead]):
    """
    Response envelope DTO for single ApplicationSetting entity payload.
    """
    pass


class ApplicationSettingListResponse(PaginatedResponse[ApplicationSettingRead]):
    """
    Response envelope DTO for paginated ApplicationSetting entities payload.
    """
    pass
