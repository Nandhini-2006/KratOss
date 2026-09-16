from fastapi import APIRouter, HTTPException

from .service import analyze_scan

router = APIRouter(
    prefix="/vulnerabilities",
    tags=["Vulnerabilities"]
)


@router.post("/analyze")
def analyze_vulnerabilities(scan_result: dict):
    try:
        result = analyze_scan(scan_result)

        return {
            "message": "Vulnerability analysis completed",
            "result": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Analysis failed: {str(error)}"
        )