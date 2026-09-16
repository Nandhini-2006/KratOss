from .analyzer import analyze_findings
from .risk import calculate_risk, calculate_overall_risk
from .recommendations import get_recommendation


def analyze_scan(scan_result):
    findings = scan_result.get("crypto_assets", [])

    vulnerabilities = analyze_findings(findings)

    for vulnerability in vulnerabilities:
        risk = calculate_risk(
            vulnerability["status"]
        )

        vulnerability["risk_level"] = risk["risk_level"]
        vulnerability["risk_score"] = risk["risk_score"]

        vulnerability["recommendation"] = get_recommendation(
            vulnerability["algorithm"]
        )

    overall_risk = calculate_overall_risk(
        vulnerabilities
    )

    return {
        "project_id": scan_result["project_id"],
        "total_findings": len(vulnerabilities),
        "overall_risk": overall_risk,
        "vulnerabilities": vulnerabilities
    }