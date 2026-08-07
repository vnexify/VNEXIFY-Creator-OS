from typing import Optional, List, Dict, Any
from pydantic import Field
from .base import BaseSchema, TimestampSchema, SuccessResponse, PaginatedResponse


class AIProviderCreate(BaseSchema):
    """
    DTO for creating a new AIProvider entity.
    """
    name: str = Field(..., min_length=2, max_length=50, description="AI provider name")
    provider_type: str = Field(..., min_length=2, max_length=50, description="Provider type identifier")
    api_endpoint: Optional[str] = Field(None, max_length=500, description="API endpoint URL")
    config_json: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Configuration JSON payload")
    is_default: bool = Field(False, description="Default provider flag")
    is_active: bool = Field(True, description="Active status flag")


class AIProviderUpdate(BaseSchema):
    """
    DTO for updating an existing AIProvider entity.
    """
    name: Optional[str] = Field(None, min_length=2, max_length=50, description="Updated provider name")
    provider_type: Optional[str] = Field(None, max_length=50, description="Updated provider type")
    api_endpoint: Optional[str] = Field(None, max_length=500, description="Updated API endpoint URL")
    config_json: Optional[Dict[str, Any]] = Field(None, description="Updated config JSON")
    is_default: Optional[bool] = Field(None, description="Updated default flag")
    is_active: Optional[bool] = Field(None, description="Updated active flag")


class AIProviderRead(TimestampSchema):
    """
    DTO for reading AIProvider entity details.
    """
    name: str = Field(..., description="Provider name")
    provider_type: str = Field(..., description="Provider type")
    api_endpoint: Optional[str] = Field(None, description="API endpoint URL")
    config_json: Optional[Dict[str, Any]] = Field(None, description="Configuration JSON payload")
    is_default: bool = Field(..., description="Default provider flag")


class AIProviderResponse(SuccessResponse[AIProviderRead]):
    """
    Response envelope DTO for single AIProvider entity payload.
    """
    pass


class AIProviderListResponse(PaginatedResponse[AIProviderRead]):
    """
    Response envelope DTO for paginated AIProvider entities payload.
    """
    pass
