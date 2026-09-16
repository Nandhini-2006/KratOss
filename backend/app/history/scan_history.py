scan_history = []


def save_scan(
    project_id: int,
    risk_level: str,
    risk_score: int,
    total_findings: int
):

    record = {
        "id": len(scan_history) + 1,
        "project_id": project_id,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "total_findings": total_findings
    }

    scan_history.append(record)

    return record


def get_project_scan_history(
    project_id: int
):

    return [
        scan
        for scan in scan_history
        if scan["project_id"] == project_id
    ]