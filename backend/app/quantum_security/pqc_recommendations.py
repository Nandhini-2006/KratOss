def build_recommendation_context(
    algorithm: str,
    file: str,
    line: int,
    quantum_risk: dict,
    mosca_risk: dict
) -> dict:

    return {
        "algorithm": algorithm,
        "file": file,
        "line": line,
        "quantum_risk": quantum_risk,
        "mosca_risk": mosca_risk
    }