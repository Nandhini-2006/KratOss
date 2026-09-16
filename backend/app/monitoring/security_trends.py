def calculate_security_trends(
    scan_history: list
) -> dict:

    if not scan_history:
        return {
            "total_scans": 0,
            "risk_scores": [],
            "finding_counts": [],
            "trend": "NO_DATA"
        }

    risk_scores = []
    finding_counts = []

    for scan in scan_history:

        risk_scores.append(
            scan.get("risk_score", 0)
        )

        finding_counts.append(
            scan.get("total_findings", 0)
        )

    trend = determine_trend(
        risk_scores
    )

    return {
        "total_scans": len(scan_history),
        "risk_scores": risk_scores,
        "finding_counts": finding_counts,
        "trend": trend
    }


def determine_trend(
    risk_scores: list
) -> str:

    if len(risk_scores) < 2:
        return "INSUFFICIENT_DATA"

    first_score = risk_scores[0]
    latest_score = risk_scores[-1]

    if latest_score < first_score:
        return "IMPROVING"

    if latest_score > first_score:
        return "INCREASING_RISK"

    return "STABLE"