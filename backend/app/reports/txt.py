def create_txt_report(cbom: dict) -> str:

    lines = []

    lines.append("KRATOS - CRYPTOGRAPHIC SECURITY REPORT")
    lines.append("=" * 50)

    lines.append(
        f"Project ID: {cbom.get('project_id')}"
    )

    lines.append(
        f"CBOM Version: {cbom.get('cbom_version')}"
    )

    lines.append(
        f"Generated At: {cbom.get('generated_at')}"
    )

    lines.append("")
    lines.append("SUMMARY")
    lines.append("-" * 30)

    summary = cbom.get("summary", {})

    lines.append(
        f"Total Crypto Assets: "
        f"{summary.get('total_crypto_assets', 0)}"
    )

    lines.append(
        f"Total Vulnerabilities: "
        f"{summary.get('total_vulnerabilities', 0)}"
    )

    lines.append(
        f"Total Quantum Findings: "
        f"{summary.get('total_quantum_findings', 0)}"
    )

    lines.append("")
    lines.append("CRYPTOGRAPHIC ASSETS")
    lines.append("-" * 30)

    for index, asset in enumerate(
        cbom.get("crypto_assets", []),
        start=1
    ):

        lines.append("")
        lines.append(f"Asset {index}")

        lines.append(
            f"Algorithm: {asset.get('algorithm')}"
        )

        lines.append(
            f"File: {asset.get('file')}"
        )

        lines.append(
            f"Line: {asset.get('line')}"
        )

        vulnerability = asset.get(
            "vulnerability",
            {}
        )

        lines.append(
            f"Status: {vulnerability.get('status')}"
        )

        lines.append(
            f"Risk Level: "
            f"{vulnerability.get('risk_level')}"
        )

        quantum = asset.get(
            "quantum_security",
            {}
        )

        lines.append(
            f"Quantum Sensitive: "
            f"{quantum.get('quantum_sensitive')}"
        )

        lines.append(
            f"Quantum Risk: "
            f"{quantum.get('risk')}"
        )

        lines.append(
            f"Mosca Risk: "
            f"{quantum.get('mosca_risk', {}).get('risk')}"
        )

    return "\n".join(lines)