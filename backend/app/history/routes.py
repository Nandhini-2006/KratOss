from fastapi import APIRouter, HTTPException

from .service import (
    get_commit_history,
    get_history
)


router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/scans/{project_id}")
def scan_history(
    project_id: int
):

    try:

        history = get_history(
            project_id
        )

        return {
            "project_id": project_id,
            "scan_history": history
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Could not load scan history: {str(error)}"
        )


@router.get("/commits")
def commit_history(
    repository_path: str,
    limit: int = 20
):

    try:

        commits = get_commit_history(
            repository_path,
            limit
        )

        return {
            "commits": commits
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Could not load commits: {str(error)}"
        )