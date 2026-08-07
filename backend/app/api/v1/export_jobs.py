from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_export_job_service
from ...services.export_job_service import ExportJobService
from ...schemas.export_job import (
    ExportJobCreate,
    ExportJobUpdate,
    ExportJobRead,
    ExportJobResponse,
    ExportJobListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=ExportJobResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Export Job",
    description="Registers a new Export Job entity.",
)
def create_export_job(
    export_in: ExportJobCreate,
    db: Session = Depends(get_db),
    export_job_service: ExportJobService = Depends(get_export_job_service),
) -> Any:
    created_export = export_job_service.create(db, export_in.model_dump())
    return ExportJobResponse(
        success=True,
        message="Export Job created successfully",
        data=ExportJobRead.model_validate(created_export),
    )


@router.get(
    "/",
    response_model=ExportJobListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Export Jobs",
    description="Retrieves a paginated list of Export Jobs.",
)
def list_export_jobs(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    export_job_service: ExportJobService = Depends(get_export_job_service),
) -> Any:
    paginated_data = export_job_service.paginate(db, page=page, page_size=page_size)
    items_read = [ExportJobRead.model_validate(item) for item in paginated_data["items"]]
    return ExportJobListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{export_id}",
    response_model=ExportJobResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Export Job by ID",
    description="Retrieves Export Job details by primary key ID.",
)
def get_export_job(
    export_id: int,
    db: Session = Depends(get_db),
    export_job_service: ExportJobService = Depends(get_export_job_service),
) -> Any:
    export_job = export_job_service.get(db, export_id)
    if not export_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Export Job with ID {export_id} not found.",
        )
    return ExportJobResponse(
        success=True,
        message="Export Job retrieved successfully",
        data=ExportJobRead.model_validate(export_job),
    )


@router.put(
    "/{export_id}",
    response_model=ExportJobResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Export Job",
    description="Updates existing Export Job attributes.",
)
def update_export_job(
    export_id: int,
    export_in: ExportJobUpdate,
    db: Session = Depends(get_db),
    export_job_service: ExportJobService = Depends(get_export_job_service),
) -> Any:
    export_job = export_job_service.get(db, export_id)
    if not export_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Export Job with ID {export_id} not found.",
        )
    updated_export = export_job_service.update(db, export_job, export_in.model_dump(exclude_unset=True))
    return ExportJobResponse(
        success=True,
        message="Export Job updated successfully",
        data=ExportJobRead.model_validate(updated_export),
    )


@router.delete(
    "/{export_id}",
    response_model=ExportJobResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Export Job",
    description="Deletes Export Job entity by ID.",
)
def delete_export_job(
    export_id: int,
    db: Session = Depends(get_db),
    export_job_service: ExportJobService = Depends(get_export_job_service),
) -> Any:
    export_job = export_job_service.get(db, export_id)
    if not export_job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Export Job with ID {export_id} not found.",
        )
    export_job_service.delete(db, export_id)
    return ExportJobResponse(
        success=True,
        message=f"Export Job with ID {export_id} deleted successfully",
        data=None,
    )
