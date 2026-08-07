from typing import Optional, List, Dict, Any
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class ExportJobCreate(BaseSchema):
    """
    DTO for creating a new ExportJob entity.
    """
    export_format: str = Field(..., min_length=1, max_length=20, description="Export format")
    status: str = Field("pending", description="Job execution status")
    file_path: Optional[str] = Field(None, max_length=500, description="Export output file path")
    user_id: int = Field(..., description="User ID initiating export")
    metadata_json: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Metadata JSON payload")
    is_active: bool = Field(True, description="Active status flag")


class ExportJobUpdate(BaseSchema):
    """
    DTO for updating an existing ExportJob entity.
    """
    status: Optional[str] = Field(None, description="Updated job execution status")
    file_path: Optional[str] = Field(None, max_length=500, description="Updated file path")
    metadata_json: Optional[Dict[str, Any]] = Field(None, description="Updated metadata JSON")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class ExportJobRead(TimestampSchema):
    """
    DTO for reading ExportJob entity details.
    """
    export_format: str = Field(..., description="Export format")
    status: str = Field(..., description="Execution status")
    file_path: Optional[str] = Field(None, description="Output file path")
    user_id: int = Field(..., description="User ID")
    metadata_json: Optional[Dict[str, Any]] = Field(None, description="Metadata JSON payload")


class ExportJobResponse(SuccessResponse[ExportJobRead]):
    """
    Response envelope DTO for single ExportJob entity payload.
    """
    pass


class ExportJobListResponse(PaginatedResponse[ExportJobRead]):
    """
    Response envelope DTO for paginated ExportJob entities payload.
    """
    pass
