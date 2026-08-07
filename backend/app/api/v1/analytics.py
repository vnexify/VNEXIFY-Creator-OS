from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_analytics_service
from ...services.analytics_service import AnalyticsService
from ...schemas.analytics import (
    AnalyticsCreate,
    AnalyticsUpdate,
    AnalyticsRead,
    AnalyticsResponse,
    AnalyticsListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=AnalyticsResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Analytics Record",
    description="Registers a new Analytics content performance record.",
)
def create_analytics(
    analytics_in: AnalyticsCreate,
    db: Session = Depends(get_db),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
) -> Any:
    created_analytics = analytics_service.create(db, analytics_in.model_dump())
    return AnalyticsResponse(
        success=True,
        message="Analytics record created successfully",
        data=AnalyticsRead.model_validate(created_analytics),
    )


@router.get(
    "/",
    response_model=AnalyticsListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Analytics Records",
    description="Retrieves a paginated list of Analytics performance records.",
)
def list_analytics(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
) -> Any:
    paginated_data = analytics_service.paginate(db, page=page, page_size=page_size)
    items_read = [AnalyticsRead.model_validate(item) for item in paginated_data["items"]]
    return AnalyticsListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{analytics_id}",
    response_model=AnalyticsResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Analytics Record by ID",
    description="Retrieves Analytics record details by primary key ID.",
)
def get_analytics(
    analytics_id: int,
    db: Session = Depends(get_db),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
) -> Any:
    analytics_record = analytics_service.get(db, analytics_id)
    if not analytics_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Analytics record with ID {analytics_id} not found.",
        )
    return AnalyticsResponse(
        success=True,
        message="Analytics record retrieved successfully",
        data=AnalyticsRead.model_validate(analytics_record),
    )


@router.put(
    "/{analytics_id}",
    response_model=AnalyticsResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Analytics Record",
    description="Updates existing Analytics record attributes.",
)
def update_analytics(
    analytics_id: int,
    analytics_in: AnalyticsUpdate,
    db: Session = Depends(get_db),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
) -> Any:
    analytics_record = analytics_service.get(db, analytics_id)
    if not analytics_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Analytics record with ID {analytics_id} not found.",
        )
    updated_analytics = analytics_service.update(db, analytics_record, analytics_in.model_dump(exclude_unset=True))
    return AnalyticsResponse(
        success=True,
        message="Analytics record updated successfully",
        data=AnalyticsRead.model_validate(updated_analytics),
    )


@router.delete(
    "/{analytics_id}",
    response_model=AnalyticsResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Analytics Record",
    description="Deletes Analytics record entity by ID.",
)
def delete_analytics(
    analytics_id: int,
    db: Session = Depends(get_db),
    analytics_service: AnalyticsService = Depends(get_analytics_service),
) -> Any:
    analytics_record = analytics_service.get(db, analytics_id)
    if not analytics_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Analytics record with ID {analytics_id} not found.",
        )
    analytics_service.delete(db, analytics_id)
    return AnalyticsResponse(
        success=True,
        message=f"Analytics record with ID {analytics_id} deleted successfully",
        data=None,
    )
