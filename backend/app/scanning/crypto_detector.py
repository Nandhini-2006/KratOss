import os
import re


CRYPTO_PATTERNS = {
    "MD5": r"\bMD5\b|md5\(",
    "SHA-1": r"\bSHA[-_]?1\b|sha1\(",
    "SHA-256": r"\bSHA[-_]?256\b|sha256\(",
    "RSA": r"\bRSA\b|RSA/ECB|RSA/PKCS",
    "AES": r"\bAES\b|AES/",
    "DES": r"\bDES\b",
    "3DES": r"\b3DES\b|DESede",
    "ECDSA": r"\bECDSA\b",
    "ECDH": r"\bECDH\b",
    "Diffie-Hellman": r"\bDiffie[- ]Hellman\b",
}


def scan_file(file_path: str):

    findings = []

    try:
        with open(
            file_path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:

            content = file.read()

    except Exception:
        return findings

    for algorithm, pattern in CRYPTO_PATTERNS.items():

        matches = re.finditer(
            pattern,
            content,
            re.IGNORECASE
        )

        for match in matches:

            line_number = content[:match.start()].count("\n") + 1

            findings.append({
                "algorithm": algorithm,
                "file": file_path,
                "line": line_number
            })

    return findings


def scan_repository(repository_path: str):

    findings = []

    ignored = {
        ".git",
        "node_modules",
        "__pycache__",
        ".venv"
    }

    for root, directories, files in os.walk(repository_path):

        directories[:] = [
            d for d in directories
            if d not in ignored
        ]

        for filename in files:

            file_path = os.path.join(root, filename)

            findings.extend(
                scan_file(file_path)
            )

    return findings