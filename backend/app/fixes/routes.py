from fastapi import APIRouter, HTTPException

from .service import (
    prepare_fix,
    prepare_multiple_fixes
)


router = APIRouter(
    prefix="/fixes",
    tags=["Fixes"]
)


@router.post("/suggest")
def suggest_fix(
    vulnerability: dict
):

    try:

        result = prepare_fix(
            vulnerability
        )

        return {
            "message": "Fix context prepared successfully",
            "result": result
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Fix preparation failed: {str(error)}"
        )


@router.post("/suggest-all")
def suggest_all_fixes(
    vulnerabilities: list
):

    try:

        result = prepare_multiple_fixes(
            vulnerabilities
        )

        return {
            "message": "Fix contexts prepared successfully",
            "total": len(result),
            "results": result
        }

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Fix preparation failed: {str(error)}"
        )