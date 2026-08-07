from typing import Optional, List
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class MediaCreate(BaseSchema):
    """
    DTO for creating a new Media entity.
    """
    filename: str = Field(..., min_length=1, max_length=255, description="Original media filename")
    file_path: str = Field(..., min_length=1, max_length=500, description="Relative storage file path")
    file_size: int = Field(..., ge=0, description="File size in bytes")
    mime_type: str = Field(..., min_length=1, max_length=100, description="MIME type string")
    file_hash: Optional[str] = Field(None, max_length=64, description="Unique SHA256 file hash")
    workspace_id: int = Field(..., description="Parent workspace ID")
    uploader_id: int = Field(..., description="Uploader user ID")
    is_active: bool = Field(True, description="Active status flag")


class MediaUpdate(BaseSchema):
    """
    DTO for updating an existing Media entity.
    """
    filename: Optional[str] = Field(None, min_length=1, max_length=255, description="Updated filename")
    file_path: Optional[str] = Field(None, min_length=1, max_length=500, description="Updated file path")
    file_size: Optional[int] = Field(None, ge=0, description="Updated file size")
    mime_type: Optional[str] = Field(None, max_length=100, description="Updated MIME type")
    is_active: Optional[bool] = Field(None, description="Updated active status flag")


class MediaRead(TimestampSchema):
    """
    DTO for reading Media entity details.
    """
    filename: str = Field(..., description="Original filename")
    file_path: str = Field(..., description="Storage file path")
    file_size: int = Field(..., description="File size in bytes")
    mime_type: str = Field(..., description="MIME type")
    file_hash: Optional[str] = Field(None, description="SHA256 file hash")
    workspace_id: int = Field(..., description="Parent workspace ID")
    uploader_id: int = Field(..., description="Uploader user ID")


class MediaResponse(SuccessResponse[MediaRead]):
    """
    Response envelope DTO for single Media entity payload.
    """
    pass


class MediaListResponse(PaginatedResponse[MediaRead]):
    """
    Response envelope DTO for paginated Media entities payload.
    """
    pass
