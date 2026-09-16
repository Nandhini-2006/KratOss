def analyze_finding(finding):
    algorithm = finding["algorithm"]

    weak_algorithms = {
        "MD5",
        "SHA-1",
        "DES",
        "3DES"
    }

    quantum_sensitive = {
        "RSA",
        "ECDSA",
        "ECDH",
        "Diffie-Hellman"
    }

    if algorithm in weak_algorithms:
        return {
            "algorithm": algorithm,
            "status": "Vulnerable",
            "reason": "Weak or deprecated cryptographic algorithm"
        }

    if algorithm in quantum_sensitive:
        return {
            "algorithm": algorithm,
            "status": "Quantum Risk",
            "reason": "Potentially vulnerable to future quantum attacks"
        }

    return {
        "algorithm": algorithm,
        "status": "Review",
        "reason": "Cryptographic usage should be reviewed"
    }


def analyze_findings(findings):
    results = []

    for finding in findings:
        result = analyze_finding(finding)

        result["file"] = finding["file"]
        result["line"] = finding["line"]

        results.append(result)

    return results