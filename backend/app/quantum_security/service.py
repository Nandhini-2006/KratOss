from .quantum_risk import check_quantum_risk
from .mosca import calculate_mosca_risk
from .pqc_recommendations import build_recommendation_context


def analyze_quantum_security(
    analysis_result: dict,
    data_lifetime_years: int = 10,
    migration_time_years: int = 5,
    quantum_arrival_years: int = 15
):

    vulnerabilities = analysis_result.get(
        "vulnerabilities",
        []
    )

    results = []

    for vulnerability in vulnerabilities:

        algorithm = vulnerability["algorithm"]

        quantum_risk = check_quantum_risk(
            algorithm
        )

        mosca_risk = calculate_mosca_risk(
            data_lifetime_years,
            migration_time_years,
            quantum_arrival_years
        )

        ai_context = build_recommendation_context(
            algorithm=algorithm,
            file=vulnerability["file"],
            line=vulnerability["line"],
            quantum_risk=quantum_risk,
            mosca_risk=mosca_risk
        )

        results.append({
            "algorithm": algorithm,
            "file": vulnerability["file"],
            "line": vulnerability["line"],
            "quantum_risk": quantum_risk,
            "mosca_risk": mosca_risk,
            "ai_context": ai_context
        })

    return {
        "project_id": analysis_result["project_id"],
        "total_findings": len(results),
        "quantum_findings": results
    }