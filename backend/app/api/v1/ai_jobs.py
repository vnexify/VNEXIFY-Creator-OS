from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_ai_job_service
from ...services.ai_job_service import AIJobService
from ...schemas.ai_job import (
    AIJobCreate,
    AIJobUpdate,
    AIJobRead,
    AIJobResponse,
    AIJobListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=AIJobResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create AI Job",
    description="Registers a new AI Job execution log entry.",
)
def create_ai_job(
    job_in: AIJobCreate,
    db: Session = Depends(get_db),
    ai_job_service: AIJobService = Depends(get_ai_job_service),
) -> Any:
    created_job = ai_job_service.create(db, job_in.model_dump())
    return AIJobResponse(
        success=True,
        message="AI Job created successfully",
        data=AIJobRead.model_validate(created_job),
    )


@router.get(
    "/",
    response_model=AIJobListResponse,
    status_code=status.HTTP_200_OK,
    summary="List AI Jobs",
    description="Retrieves a paginated list of AI Jobs.",
)
def list_ai_jobs(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    ai_job_service: AIJobService = Depends(get_ai_job_service),
) -> Any:
    paginated_data = ai_job_service.paginate(db, page=page, page_size=page_size)
    items_read = [AIJobRead.model_validate(item) for item in paginated_data["items"]]
    return AIJobListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{job_id}",
    response_model=AIJobResponse,
    status_code=status.HTTP_200_OK,
    summary="Get AI Job by ID",
    description="Retrieves AI Job details by primary key ID.",
)
def get_ai_job(
    job_id: int,
    db: Session = Depends(get_db),
    ai_job_service: AIJobService = Depends(get_ai_job_service),
) -> Any:
    job = ai_job_service.get(db, job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AI Job with ID {job_id} not found.",
        )
    return AIJobResponse(
        success=True,
        message="AI Job retrieved successfully",
        data=AIJobRead.model_validate(job),
    )


@router.put(
    "/{job_id}",
    response_model=AIJobResponse,
    status_code=status.HTTP_200_OK,
    summary="Update AI Job",
    description="Updates existing AI Job attributes.",
)
def update_ai_job(
    job_id: int,
    job_in: AIJobUpdate,
    db: Session = Depends(get_db),
    ai_job_service: AIJobService = Depends(get_ai_job_service),
) -> Any:
    job = ai_job_service.get(db, job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AI Job with ID {job_id} not found.",
        )
    updated_job = ai_job_service.update(db, job, job_in.model_dump(exclude_unset=True))
    return AIJobResponse(
        success=True,
        message="AI Job updated successfully",
        data=AIJobRead.model_validate(updated_job),
    )


@router.delete(
    "/{job_id}",
    response_model=AIJobResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete AI Job",
    description="Deletes AI Job entity by ID.",
)
def delete_ai_job(
    job_id: int,
    db: Session = Depends(get_db),
    ai_job_service: AIJobService = Depends(get_ai_job_service),
) -> Any:
    job = ai_job_service.get(db, job_id)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AI Job with ID {job_id} not found.",
        )
    ai_job_service.delete(db, job_id)
    return AIJobResponse(
        success=True,
        message=f"AI Job with ID {job_id} deleted successfully",
        data=None,
    )
