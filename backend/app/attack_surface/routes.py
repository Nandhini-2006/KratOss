from fastapi import APIRouter, HTTPException

from .service import generate_attack_surface


router = APIRouter(
    prefix="/attack-surface",
    tags=["Attack Surface"]
)


@router.post("/map")
def map_attack_surface(analysis_result: dict):
    try:
        result = generate_attack_surface(
            analysis_result
        )

        return {
            "message": "Attack surface generated successfully",
            "result": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Attack surface generation failed: {str(error)}"
        )