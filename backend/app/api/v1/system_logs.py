from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_system_log_service
from ...services.system_log_service import SystemLogService
from ...schemas.system_log import (
    SystemLogCreate,
    SystemLogUpdate,
    SystemLogRead,
    SystemLogResponse,
    SystemLogListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=SystemLogResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create System Log Entry",
    description="Registers a new SystemLog diagnostic log entry.",
)
def create_system_log(
    log_in: SystemLogCreate,
    db: Session = Depends(get_db),
    log_service: SystemLogService = Depends(get_system_log_service),
) -> Any:
    created_log = log_service.create(db, log_in.model_dump())
    return SystemLogResponse(
        success=True,
        message="System log created successfully",
        data=SystemLogRead.model_validate(created_log),
    )


@router.get(
    "/",
    response_model=SystemLogListResponse,
    status_code=status.HTTP_200_OK,
    summary="List System Logs",
    description="Retrieves a paginated list of System Logs.",
)
def list_system_logs(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    log_service: SystemLogService = Depends(get_system_log_service),
) -> Any:
    paginated_data = log_service.paginate(db, page=page, page_size=page_size)
    items_read = [SystemLogRead.model_validate(item) for item in paginated_data["items"]]
    return SystemLogListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{log_id}",
    response_model=SystemLogResponse,
    status_code=status.HTTP_200_OK,
    summary="Get System Log by ID",
    description="Retrieves System Log details by primary key ID.",
)
def get_system_log(
    log_id: int,
    db: Session = Depends(get_db),
    log_service: SystemLogService = Depends(get_system_log_service),
) -> Any:
    system_log = log_service.get(db, log_id)
    if not system_log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"System log with ID {log_id} not found.",
        )
    return SystemLogResponse(
        success=True,
        message="System log retrieved successfully",
        data=SystemLogRead.model_validate(system_log),
    )


@router.put(
    "/{log_id}",
    response_model=SystemLogResponse,
    status_code=status.HTTP_200_OK,
    summary="Update System Log",
    description="Updates existing System Log attributes.",
)
def update_system_log(
    log_id: int,
    log_in: SystemLogUpdate,
    db: Session = Depends(get_db),
    log_service: SystemLogService = Depends(get_system_log_service),
) -> Any:
    system_log = log_service.get(db, log_id)
    if not system_log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"System log with ID {log_id} not found.",
        )
    updated_log = log_service.update(db, system_log, log_in.model_dump(exclude_unset=True))
    return SystemLogResponse(
        success=True,
        message="System log updated successfully",
        data=SystemLogRead.model_validate(updated_log),
    )


@router.delete(
    "/{log_id}",
    response_model=SystemLogResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete System Log",
    description="Deletes System Log entity by ID.",
)
def delete_system_log(
    log_id: int,
    db: Session = Depends(get_db),
    log_service: SystemLogService = Depends(get_system_log_service),
) -> Any:
    system_log = log_service.get(db, log_id)
    if not system_log:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"System log with ID {log_id} not found.",
        )
    log_service.delete(db, log_id)
    return SystemLogResponse(
        success=True,
        message=f"System log with ID {log_id} deleted successfully",
        data=None,
    )
