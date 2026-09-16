from fastapi import APIRouter, HTTPException

from .service import create_cbom


router = APIRouter(
    prefix="/cbom",
    tags=["CBOM"]
)


@router.post("/generate")
def generate_cbom_route(
    scan_result: dict,
    vulnerability_result: dict,
    quantum_result: dict
):

    try:

        result = create_cbom(
            scan_result,
            vulnerability_result,
            quantum_result
        )

        if not result["valid"]:

            raise HTTPException(
                status_code=400,
                detail=result["validation"]
            )

        return {
            "message": "CBOM generated successfully",
            "result": result
        }

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"CBOM generation failed: {str(error)}"
        )