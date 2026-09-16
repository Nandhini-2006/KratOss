from fastapi import APIRouter, HTTPException

from .service import scan_project


router = APIRouter(
    prefix="/scanning",
    tags=["Scanning"]
)


@router.post("/{project_id}")
def start_scan(
    project_id: int,
    repo_url: str
):

    try:

        result = scan_project(
            repo_url,
            project_id
        )

        return {
            "message": "Scan completed successfully",
            "result": result
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Scan failed: {str(error)}"
        )