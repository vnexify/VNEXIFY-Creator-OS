from typing import Generic, TypeVar, Optional, List, Dict, Any
from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict, Field

DataType = TypeVar("DataType")


class BaseSchema(BaseModel):
    """
    Root base schema configured for Pydantic v2 ORM mode and attribute parsing.
    """
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        use_enum_values=True,
    )


class UUIDSchema(BaseSchema):
    """
    Base schema for entities featuring primary key ID and UUID string.
    """
    id: int = Field(..., description="Primary key integer identifier")
    uuid: str = Field(..., description="Unique UUID string identifier")


class TimestampSchema(UUIDSchema):
    """
    Base schema for entities extending BaseEntity audit timestamps.
    """
    is_active: bool = Field(True, description="Active entity flag")
    created_at: datetime = Field(..., description="Creation UTC timestamp")
    updated_at: datetime = Field(..., description="Last update UTC timestamp")


class PaginationMeta(BaseSchema):
    """
    Pagination metadata summary DTO.
    """
    page: int = Field(1, ge=1, description="Current page number")
    page_size: int = Field(20, ge=1, le=100, description="Items per page")
    total: int = Field(0, ge=0, description="Total record count")
    total_pages: int = Field(0, ge=0, description="Total page count")
    has_next: bool = Field(False, description="Has next page indicator")
    has_previous: bool = Field(False, description="Has previous page indicator")


class PaginatedResponse(BaseSchema, Generic[DataType]):
    """
    Generic paginated list wrapper payload DTO.
    """
    items: List[DataType] = Field(default_factory=list, description="Page items list")
    total: int = Field(0, ge=0, description="Total record count")
    page: int = Field(1, ge=1, description="Current page number")
    page_size: int = Field(20, ge=1, le=100, description="Items per page")
    total_pages: int = Field(0, ge=0, description="Total page count")
    has_next: bool = Field(False, description="Has next page indicator")
    has_previous: bool = Field(False, description="Has previous page indicator")


class SuccessResponse(BaseSchema, Generic[DataType]):
    """
    Generic API success response envelope DTO.
    """
    success: bool = Field(True, description="Operation success flag")
    message: str = Field("Operation completed successfully", description="Status message")
    data: Optional[DataType] = Field(None, description="Response payload data")


class ErrorResponse(BaseSchema):
    """
    Standardized API error response envelope DTO.
    """
    success: bool = Field(False, description="Operation failure flag")
    error_code: str = Field(..., description="Machine-readable error code")
    message: str = Field(..., description="Human-readable error description")
    details: Optional[List[Dict[str, Any]]] = Field(None, description="Detailed validation error list")
