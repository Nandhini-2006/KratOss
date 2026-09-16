def calculate_risk(status):
    if status == "Vulnerable":
        return {
            "risk_level": "HIGH",
            "risk_score": 90
        }

    if status == "Quantum Risk":
        return {
            "risk_level": "MEDIUM",
            "risk_score": 70
        }

    return {
        "risk_level": "LOW",
        "risk_score": 30
    }


def calculate_overall_risk(vulnerabilities):
    if not vulnerabilities:
        return {
            "risk_score": 0,
            "risk_level": "SAFE"
        }

    scores = [
        calculate_risk(v["status"])["risk_score"]
        for v in vulnerabilities
    ]

    score = max(scores)

    if score >= 80:
        level = "HIGH"
    elif score >= 60:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "risk_score": score,
        "risk_level": level
    }