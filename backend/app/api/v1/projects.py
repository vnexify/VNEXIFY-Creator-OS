from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_project_service
from ...services.project_service import ProjectService
from ...schemas.project import (
    ProjectCreate,
    ProjectUpdate,
    ProjectRead,
    ProjectResponse,
    ProjectListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Project",
    description="Creates a new Project entity.",
)
def create_project(
    project_in: ProjectCreate,
    db: Session = Depends(get_db),
    project_service: ProjectService = Depends(get_project_service),
) -> Any:
    existing_proj = project_service.get_by_slug(db, project_in.workspace_id, project_in.slug)
    if existing_proj:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Project with slug '{project_in.slug}' already exists in workspace {project_in.workspace_id}.",
        )
    created_proj = project_service.create(db, project_in.model_dump())
    return ProjectResponse(
        success=True,
        message="Project created successfully",
        data=ProjectRead.model_validate(created_proj),
    )


@router.get(
    "/",
    response_model=ProjectListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Projects",
    description="Retrieves a paginated list of Projects.",
)
def list_projects(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    project_service: ProjectService = Depends(get_project_service),
) -> Any:
    paginated_data = project_service.paginate(db, page=page, page_size=page_size)
    items_read = [ProjectRead.model_validate(item) for item in paginated_data["items"]]
    return ProjectListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Project by ID",
    description="Retrieves Project details by primary key ID.",
)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    project_service: ProjectService = Depends(get_project_service),
) -> Any:
    project = project_service.get(db, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found.",
        )
    return ProjectResponse(
        success=True,
        message="Project retrieved successfully",
        data=ProjectRead.model_validate(project),
    )


@router.put(
    "/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Project",
    description="Updates existing Project attributes.",
)
def update_project(
    project_id: int,
    project_in: ProjectUpdate,
    db: Session = Depends(get_db),
    project_service: ProjectService = Depends(get_project_service),
) -> Any:
    project = project_service.get(db, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found.",
        )
    updated_proj = project_service.update(db, project, project_in.model_dump(exclude_unset=True))
    return ProjectResponse(
        success=True,
        message="Project updated successfully",
        data=ProjectRead.model_validate(updated_proj),
    )


@router.delete(
    "/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Project",
    description="Deletes Project entity by ID.",
)
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    project_service: ProjectService = Depends(get_project_service),
) -> Any:
    project = project_service.get(db, project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project with ID {project_id} not found.",
        )
    project_service.delete(db, project_id)
    return ProjectResponse(
        success=True,
        message=f"Project with ID {project_id} deleted successfully",
        data=None,
    )
