from fastapi import APIRouter, HTTPException

from .service import get_security_monitoring


router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring"]
)


@router.post("/trends")
def security_trends(
    scan_history: list
):

    try:

        result = get_security_monitoring(
            scan_history
        )

        return {
            "message": "Security trends calculated successfully",
            "result": result
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Monitoring failed: {str(error)}"
        )