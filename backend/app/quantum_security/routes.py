from fastapi import APIRouter, HTTPException

from .service import analyze_quantum_security


router = APIRouter(
    prefix="/quantum-security",
    tags=["Quantum Security"]
)


@router.post("/analyze")
def analyze_quantum_security_route(
    analysis_result: dict
):

    try:

        result = analyze_quantum_security(
            analysis_result
        )

        return {
            "message": "Quantum security analysis completed",
            "result": result
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Quantum analysis failed: {str(error)}"
        )