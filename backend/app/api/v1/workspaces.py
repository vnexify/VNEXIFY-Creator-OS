from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from ..deps import get_db, get_workspace_service
from ...services.workspace_service import WorkspaceService
from ...schemas.workspace import (
    WorkspaceCreate,
    WorkspaceUpdate,
    WorkspaceRead,
    WorkspaceResponse,
    WorkspaceListResponse,
)

router = APIRouter()


@router.post(
    "/",
    response_model=WorkspaceResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Workspace",
    description="Creates a new Workspace entity.",
)
def create_workspace(
    workspace_in: WorkspaceCreate,
    db: Session = Depends(get_db),
    workspace_service: WorkspaceService = Depends(get_workspace_service),
) -> Any:
    existing_ws = workspace_service.get_by_slug(db, workspace_in.slug)
    if existing_ws:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Workspace with slug '{workspace_in.slug}' already exists.",
        )
    created_ws = workspace_service.create(db, workspace_in.model_dump())
    return WorkspaceResponse(
        success=True,
        message="Workspace created successfully",
        data=WorkspaceRead.model_validate(created_ws),
    )


@router.get(
    "/",
    response_model=WorkspaceListResponse,
    status_code=status.HTTP_200_OK,
    summary="List Workspaces",
    description="Retrieves a paginated list of Workspaces.",
)
def list_workspaces(
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    db: Session = Depends(get_db),
    workspace_service: WorkspaceService = Depends(get_workspace_service),
) -> Any:
    paginated_data = workspace_service.paginate(db, page=page, page_size=page_size)
    items_read = [WorkspaceRead.model_validate(item) for item in paginated_data["items"]]
    return WorkspaceListResponse(
        items=items_read,
        total=paginated_data["total"],
        page=paginated_data["page"],
        page_size=paginated_data["page_size"],
        total_pages=paginated_data["total_pages"],
        has_next=paginated_data["has_next"],
        has_previous=paginated_data["has_previous"],
    )


@router.get(
    "/{workspace_id}",
    response_model=WorkspaceResponse,
    status_code=status.HTTP_200_OK,
    summary="Get Workspace by ID",
    description="Retrieves Workspace details by primary key ID.",
)
def get_workspace(
    workspace_id: int,
    db: Session = Depends(get_db),
    workspace_service: WorkspaceService = Depends(get_workspace_service),
) -> Any:
    workspace = workspace_service.get(db, workspace_id)
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workspace with ID {workspace_id} not found.",
        )
    return WorkspaceResponse(
        success=True,
        message="Workspace retrieved successfully",
        data=WorkspaceRead.model_validate(workspace),
    )


@router.put(
    "/{workspace_id}",
    response_model=WorkspaceResponse,
    status_code=status.HTTP_200_OK,
    summary="Update Workspace",
    description="Updates existing Workspace attributes.",
)
def update_workspace(
    workspace_id: int,
    workspace_in: WorkspaceUpdate,
    db: Session = Depends(get_db),
    workspace_service: WorkspaceService = Depends(get_workspace_service),
) -> Any:
    workspace = workspace_service.get(db, workspace_id)
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workspace with ID {workspace_id} not found.",
        )
    updated_ws = workspace_service.update(db, workspace, workspace_in.model_dump(exclude_unset=True))
    return WorkspaceResponse(
        success=True,
        message="Workspace updated successfully",
        data=WorkspaceRead.model_validate(updated_ws),
    )


@router.delete(
    "/{workspace_id}",
    response_model=WorkspaceResponse,
    status_code=status.HTTP_200_OK,
    summary="Delete Workspace",
    description="Deletes Workspace entity by ID.",
)
def delete_workspace(
    workspace_id: int,
    db: Session = Depends(get_db),
    workspace_service: WorkspaceService = Depends(get_workspace_service),
) -> Any:
    workspace = workspace_service.get(db, workspace_id)
    if not workspace:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Workspace with ID {workspace_id} not found.",
        )
    workspace_service.delete(db, workspace_id)
    return WorkspaceResponse(
        success=True,
        message=f"Workspace with ID {workspace_id} deleted successfully",
        data=None,
    )
