import os

from .scanner import clone_repository
from .crypto_detector import scan_repository
from .dependency_scanner import find_dependency_files


BASE_SCAN_DIRECTORY = "storage/scanned_repositories"


def scan_project(repo_url: str, project_id: int):

    repository_path = os.path.join(
        BASE_SCAN_DIRECTORY,
        f"project_{project_id}"
    )

    # 1. Download repository
    clone_repository(
        repo_url,
        repository_path
    )

    # 2. Find cryptographic usage
    crypto_findings = scan_repository(
        repository_path
    )

    # 3. Find dependency files
    dependency_files = find_dependency_files(
        repository_path
    )

    return {
        "project_id": project_id,
        "crypto_assets": crypto_findings,
        "dependency_files": dependency_files,
        "total_crypto_assets": len(crypto_findings)
    }