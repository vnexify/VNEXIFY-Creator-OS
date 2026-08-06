from typing import Generic, TypeVar, Optional, List, Any
from datetime import datetime, timezone
from pydantic import BaseModel, Field

DataType = TypeVar("DataType")


class PaginationMeta(BaseModel):
    currentPage: int = 1
    pageSize: int = 20
    totalRecords: int = 0
    totalPages: int = 0
    hasNextPage: bool = False
    hasPrevPage: bool = False


class BaseMeta(BaseModel):
    requestId: str = "unknown"
    timestamp: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    pagination: Optional[PaginationMeta] = None


class BaseResponseEnvelope(BaseModel, Generic[DataType]):
    success: bool = True
    data: Optional[DataType] = None
    meta: Optional[BaseMeta] = None


class BaseErrorDetail(BaseModel):
    field: Optional[str] = None
    issue: str


class BaseErrorPayload(BaseModel):
    code: str
    message: str
    details: List[BaseErrorDetail] = []


class BaseErrorEnvelope(BaseModel):
    success: bool = False
    error: BaseErrorPayload
    meta: Optional[BaseMeta] = None
