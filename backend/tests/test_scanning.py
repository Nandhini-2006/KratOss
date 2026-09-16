from app.scanning.crypto_detector import scan_file


def test_crypto_detection(
    tmp_path
):

    file_path = tmp_path / "test.py"

    file_path.write_text(
        "hash = SHA256(data)"
    )

    findings = scan_file(
        str(file_path)
    )

    assert len(findings) > 0
    assert findings[0]["algorithm"] == "SHA-256"