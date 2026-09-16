from fastapi import APIRouter, HTTPException

from .models import ProjectCreate, ProjectUpdate
from .service import (
    create_project,
    get_projects,
    get_project,
    update_project,
    delete_project
)


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("/")
def add_project(project: ProjectCreate):

    new_project = create_project(project)

    return {
        "message": "Project created successfully",
        "project": new_project
    }


@router.get("/")
def list_projects():

    return {
        "projects": get_projects()
    }


@router.get("/{project_id}")
def project_details(project_id: int):

    project = get_project(project_id)

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return project


@router.put("/{project_id}")
def edit_project(project_id: int, project: ProjectUpdate):

    updated_project = update_project(project_id, project)

    if updated_project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project updated successfully",
        "project": updated_project
    }


@router.delete("/{project_id}")
def remove_project(project_id: int):

    deleted = delete_project(project_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project deleted successfully"
    }