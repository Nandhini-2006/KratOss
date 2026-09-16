RECOMMENDATIONS = {
    "MD5": "Replace MD5 with SHA-256 or a stronger modern hash.",
    "SHA-1": "Replace SHA-1 with SHA-256 or SHA-3.",
    "DES": "Replace DES with AES-256.",
    "3DES": "Migrate from 3DES to AES-256.",
    "RSA": "Plan migration toward post-quantum or hybrid public-key cryptography.",
    "ECDSA": "Plan migration toward post-quantum or hybrid digital signatures.",
    "ECDH": "Plan migration toward post-quantum or hybrid key establishment.",
    "Diffie-Hellman": "Plan migration toward a post-quantum or hybrid key-establishment mechanism.",
    "AES": "Review key size, mode of operation, and key-management practices."
}


def get_recommendation(algorithm):
    return RECOMMENDATIONS.get(
        algorithm,
        "Review this cryptographic implementation."
    )