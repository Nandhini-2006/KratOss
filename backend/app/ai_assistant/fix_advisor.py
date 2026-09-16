def build_fix_advisor_context(
    vulnerability: dict,
    code: str = ""
) -> dict:

    return {
        "vulnerability": {
            "algorithm": vulnerability.get(
                "algorithm"
            ),
            "status": vulnerability.get(
                "status"
            ),
            "risk_level": vulnerability.get(
                "risk_level"
            ),
            "risk_score": vulnerability.get(
                "risk_score"
            ),
            "reason": vulnerability.get(
                "reason"
            )
        },

        "location": {
            "file": vulnerability.get(
                "file"
            ),
            "line": vulnerability.get(
                "line"
            )
        },

        "code": code
    }