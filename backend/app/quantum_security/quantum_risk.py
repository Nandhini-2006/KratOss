QUANTUM_SENSITIVE_ALGORITHMS = {
    "RSA",
    "ECDSA",
    "ECDH",
    "Diffie-Hellman"
}


def check_quantum_risk(algorithm: str) -> dict:

    if algorithm in QUANTUM_SENSITIVE_ALGORITHMS:
        return {
            "quantum_sensitive": True,
            "risk": "HIGH"
        }

    return {
        "quantum_sensitive": False,
        "risk": "LOW"
    }