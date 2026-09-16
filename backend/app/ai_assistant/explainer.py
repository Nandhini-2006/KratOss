def build_explanation_context(
    vulnerability: dict
) -> dict:

    return {
        "algorithm": vulnerability.get(
            "algorithm"
        ),
        "file": vulnerability.get(
            "file"
        ),
        "line": vulnerability.get(
            "line"
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
    }