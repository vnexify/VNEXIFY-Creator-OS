from typing import Optional, List, Dict, Any
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class AIJobCreate(BaseSchema):
    """
    DTO for creating a new AIJob execution log entity.
    """
    job_type: str = Field(..., min_length=2, max_length=50, description="AI job task type")
    status: str = Field("pending", description="Job execution status")
    prompt: Optional[str] = Field(None, description="Input prompt text")
    response: Optional[str] = Field(None, description="Output response text")
    tokens_used: int = Field(0, ge=0, description="Total token consumption count")
    provider_id: int = Field(..., description="AI provider ID")
    user_id: int = Field(..., description="User ID initiating request")
    metadata_json: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata JSON payload")
    is_active: bool = Field(True, description="Active status flag")


class AIJobUpdate(BaseSchema):
    """
    DTO for updating an existing AIJob execution log entity.
    """
    status: Optional[str] = Field(None, description="Updated job execution status")
    response: Optional[str] = Field(None, description="Updated output response text")
    tokens_used: Optional[int] = Field(None, ge=0, description="Updated tokens count")
    metadata_json: Optional[Dict[str, Any]] = Field(None, description="Updated metadata JSON")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class AIJobRead(TimestampSchema):
    """
    DTO for reading AIJob execution log details.
    """
    job_type: str = Field(..., description="AI job task type")
    status: str = Field(..., description="Job execution status")
    prompt: Optional[str] = Field(None, description="Input prompt text")
    response: Optional[str] = Field(None, description="Output response text")
    tokens_used: int = Field(..., description="Token consumption count")
    provider_id: int = Field(..., description="AI provider ID")
    user_id: int = Field(..., description="User ID")
    metadata_json: Optional[Dict[str, Any]] = Field(None, description="Metadata JSON payload")


class AIJobResponse(SuccessResponse[AIJobRead]):
    """
    Response envelope DTO for single AIJob entity payload.
    """
    pass


class AIJobListResponse(PaginatedResponse[AIJobRead]):
    """
    Response envelope DTO for paginated AIJob entities payload.
    """
    pass
