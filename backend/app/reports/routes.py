from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from .service import generate_report


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.post("/generate")
def generate_report_route(
    cbom: dict,
    report_format: str = "json"
):

    try:

        project_id = cbom.get(
            "project_id"
        )

        if project_id is None:
            raise HTTPException(
                status_code=400,
                detail="Project ID is required"
            )

        if report_format not in {
            "json",
            "txt",
            "pdf"
        }:

            raise HTTPException(
                status_code=400,
                detail="Format must be json, txt or pdf"
            )

        report_path = generate_report(
            cbom,
            report_format,
            project_id
        )

        return FileResponse(
            path=report_path,
            filename=report_path.split("/")[-1]
        )

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Report generation failed: {str(error)}"
        )