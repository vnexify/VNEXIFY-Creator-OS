from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_schedule_service
from ...services.schedule_service import ScheduleService
from ...schemas.schedule import (
    ScheduleCreate,
    ScheduleUpdate,
    ScheduleRead,
    ScheduleResponse,
    ScheduleListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=ScheduleResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Schedule",
    description="Creates a new publication Schedule entity.",
)
def create_schedule(
    schedule_in: ScheduleCreate,
    db: Session = Depends(get_db),
    schedule_service: ScheduleService = Depends(get_schedule_service),
) -> Any:
    created_schedule = schedule_service.create(db, schedule_in.model_dump())
    return ScheduleResponse(
        success=True,
        message="Schedule created successfully",
        data=ScheduleRead.model_validate(created_schedule),
    )


@router.get(
    "/",
    response_model=ScheduleListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Schedules",
    description="Retrieves a paginated list of publication Schedules.",
)
def list_schedules(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    schedule_service: ScheduleService = Depends(get_schedule_service),
) -> Any:
    paginated_data = schedule_service.paginate(db, page=page, page_size=page_size)
    items_read = [ScheduleRead.model_validate(item) for item in paginated_data["items"]]
    return ScheduleListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{schedule_id}",
    response_model=ScheduleResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Schedule by ID",
    description="Retrieves Schedule details by primary key ID.",
)
def get_schedule(
    schedule_id: int,
    db: Session = Depends(get_db),
    schedule_service: ScheduleService = Depends(get_schedule_service),
) -> Any:
    schedule_item = schedule_service.get(db, schedule_id)
    if not schedule_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Schedule with ID {schedule_id} not found.",
        )
    return ScheduleResponse(
        success=True,
        message="Schedule retrieved successfully",
        data=ScheduleRead.model_validate(schedule_item),
    )


@router.put(
    "/{schedule_id}",
    response_model=ScheduleResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Schedule",
    description="Updates existing Schedule attributes.",
)
def update_schedule(
    schedule_id: int,
    schedule_in: ScheduleUpdate,
    db: Session = Depends(get_db),
    schedule_service: ScheduleService = Depends(get_schedule_service),
) -> Any:
    schedule_item = schedule_service.get(db, schedule_id)
    if not schedule_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Schedule with ID {schedule_id} not found.",
        )
    updated_schedule = schedule_service.update(db, schedule_item, schedule_in.model_dump(exclude_unset=True))
    return ScheduleResponse(
        success=True,
        message="Schedule updated successfully",
        data=ScheduleRead.model_validate(updated_schedule),
    )


@router.delete(
    "/{schedule_id}",
    response_model=ScheduleResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Schedule",
    description="Deletes Schedule entity by ID.",
)
def delete_schedule(
    schedule_id: int,
    db: Session = Depends(get_db),
    schedule_service: ScheduleService = Depends(get_schedule_service),
) -> Any:
    schedule_item = schedule_service.get(db, schedule_id)
    if not schedule_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Schedule with ID {schedule_id} not found.",
        )
    schedule_service.delete(db, schedule_id)
    return ScheduleResponse(
        success=True,
        message=f"Schedule with ID {schedule_id} deleted successfully",
        data=None,
    )
