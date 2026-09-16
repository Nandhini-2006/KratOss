from datetime import datetime, timezone


def generate_cbom(
    scan_result: dict,
    vulnerability_result: dict,
    quantum_result: dict
) -> dict:

    crypto_assets = scan_result.get(
        "crypto_assets",
        []
    )

    vulnerabilities = vulnerability_result.get(
        "vulnerabilities",
        []
    )

    quantum_findings = quantum_result.get(
        "quantum_findings",
        []
    )

    assets = []

    for finding in crypto_assets:

        algorithm = finding.get("algorithm")
        file = finding.get("file")
        line = finding.get("line")

        vulnerability = find_matching_vulnerability(
            algorithm,
            file,
            line,
            vulnerabilities
        )

        quantum = find_matching_quantum_finding(
            algorithm,
            file,
            line,
            quantum_findings
        )

        asset = {
            "algorithm": algorithm,
            "file": file,
            "line": line,

            "vulnerability": {
                "status": vulnerability.get("status"),
                "risk_level": vulnerability.get("risk_level"),
                "risk_score": vulnerability.get("risk_score")
            },

            "quantum_security": {
                "quantum_sensitive": quantum.get(
                    "quantum_risk",
                    {}
                ).get("quantum_sensitive"),

                "risk": quantum.get(
                    "quantum_risk",
                    {}
                ).get("risk"),

                "mosca_risk": quantum.get(
                    "mosca_risk",
                    {}
                )
            }
        }

        assets.append(asset)

    return {
        "cbom_version": "1.0",
        "generated_at": datetime.now(
            timezone.utc
        ).isoformat(),

        "project_id": scan_result.get(
            "project_id"
        ),

        "summary": {
            "total_crypto_assets": len(assets),
            "total_vulnerabilities": len(vulnerabilities),
            "total_quantum_findings": len(
                quantum_findings
            )
        },

        "crypto_assets": assets,

        "dependency_files": scan_result.get(
            "dependency_files",
            []
        )
    }


def find_matching_vulnerability(
    algorithm,
    file,
    line,
    vulnerabilities
):

    for vulnerability in vulnerabilities:

        if (
            vulnerability.get("algorithm") == algorithm
            and vulnerability.get("file") == file
            and vulnerability.get("line") == line
        ):
            return vulnerability

    return {}


def find_matching_quantum_finding(
    algorithm,
    file,
    line,
    quantum_findings
):

    for finding in quantum_findings:

        if (
            finding.get("algorithm") == algorithm
            and finding.get("file") == file
            and finding.get("line") == line
        ):
            return finding

    return {}