from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_ai_provider_service
from ...services.ai_provider_service import AIProviderService
from ...schemas.ai_provider import (
    AIProviderCreate,
    AIProviderUpdate,
    AIProviderRead,
    AIProviderResponse,
    AIProviderListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=AIProviderResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create AI Provider",
    description="Registers a new AI Provider configuration entity.",
)
def create_ai_provider(
    provider_in: AIProviderCreate,
    db: Session = Depends(get_db),
    ai_provider_service: AIProviderService = Depends(get_ai_provider_service),
) -> Any:
    existing_provider = ai_provider_service.get_by_name(db, provider_in.name)
    if existing_provider:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"AI Provider with name '{provider_in.name}' already exists.",
        )
    created_provider = ai_provider_service.create(db, provider_in.model_dump())
    return AIProviderResponse(
        success=True,
        message="AI Provider created successfully",
        data=AIProviderRead.model_validate(created_provider),
    )


@router.get(
    "/",
    response_model=AIProviderListResponse,
    status_code=status.HTTP_200_OK,
    summary="List AI Providers",
    description="Retrieves a paginated list of AI Providers.",
)
def list_ai_providers(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    ai_provider_service: AIProviderService = Depends(get_ai_provider_service),
) -> Any:
    paginated_data = ai_provider_service.paginate(db, page=page, page_size=page_size)
    items_read = [AIProviderRead.model_validate(item) for item in paginated_data["items"]]
    return AIProviderListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{provider_id}",
    response_model=AIProviderResponse,
    status_code=status.HTTP_200_OK,
    summary="Get AI Provider by ID",
    description="Retrieves AI Provider details by primary key ID.",
)
def get_ai_provider(
    provider_id: int,
    db: Session = Depends(get_db),
    ai_provider_service: AIProviderService = Depends(get_ai_provider_service),
) -> Any:
    provider = ai_provider_service.get(db, provider_id)
    if not provider:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AI Provider with ID {provider_id} not found.",
        )
    return AIProviderResponse(
        success=True,
        message="AI Provider retrieved successfully",
        data=AIProviderRead.model_validate(provider),
    )


@router.put(
    "/{provider_id}",
    response_model=AIProviderResponse,
    status_code=status.HTTP_200_OK,
    summary="Update AI Provider",
    description="Updates existing AI Provider attributes.",
)
def update_ai_provider(
    provider_id: int,
    provider_in: AIProviderUpdate,
    db: Session = Depends(get_db),
    ai_provider_service: AIProviderService = Depends(get_ai_provider_service),
) -> Any:
    provider = ai_provider_service.get(db, provider_id)
    if not provider:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AI Provider with ID {provider_id} not found.",
        )
    updated_provider = ai_provider_service.update(db, provider, provider_in.model_dump(exclude_unset=True))
    return AIProviderResponse(
        success=True,
        message="AI Provider updated successfully",
        data=AIProviderRead.model_validate(updated_provider),
    )


@router.delete(
    "/{provider_id}",
    response_model=AIProviderResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete AI Provider",
    description="Deletes AI Provider entity by ID.",
)
def delete_ai_provider(
    provider_id: int,
    db: Session = Depends(get_db),
    ai_provider_service: AIProviderService = Depends(get_ai_provider_service),
) -> Any:
    provider = ai_provider_service.get(db, provider_id)
    if not provider:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AI Provider with ID {provider_id} not found.",
        )
    ai_provider_service.delete(db, provider_id)
    return AIProviderResponse(
        success=True,
        message=f"AI Provider with ID {provider_id} deleted successfully",
        data=None,
    )
