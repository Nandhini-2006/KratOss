from fastapi import APIRouter, HTTPException

from .service import (
    prepare_chat,
    prepare_explanation,
    prepare_fix_advice
)


router = APIRouter(
    prefix="/ai",
    tags=["AI Assistant"]
)


@router.post("/chat")
def ai_chat(
    question: str,
    security_data: dict
):

    try:

        context = prepare_chat(
            question,
            security_data
        )

        return {
            "message": "AI context prepared",
            "context": context
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"AI chat failed: {str(error)}"
        )


@router.post("/explain")
def explain_vulnerability(
    vulnerability: dict
):

    try:

        context = prepare_explanation(
            vulnerability
        )

        return {
            "message": "Explanation context prepared",
            "context": context
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Explanation failed: {str(error)}"
        )


@router.post("/fix-advice")
def fix_advice(
    vulnerability: dict,
    code: str = ""
):

    try:

        context = prepare_fix_advice(
            vulnerability,
            code
        )

        return {
            "message": "Fix advice context prepared",
            "context": context
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Fix advice failed: {str(error)}"
        )