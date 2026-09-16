from .commits import get_git_commits
from .scan_history import (
    save_scan,
    get_project_scan_history
)


def get_commit_history(
    repository_path: str,
    limit: int = 20
):

    return get_git_commits(
        repository_path,
        limit
    )


def record_scan(
    project_id: int,
    analysis_result: dict
):

    overall_risk = analysis_result.get(
        "overall_risk",
        {}
    )

    return save_scan(
        project_id=project_id,
        risk_level=overall_risk.get(
            "risk_level",
            "UNKNOWN"
        ),
        risk_score=overall_risk.get(
            "risk_score",
            0
        ),
        total_findings=analysis_result.get(
            "total_findings",
            0
        )
    )


def get_history(
    project_id: int
):

    return get_project_scan_history(
        project_id
    )