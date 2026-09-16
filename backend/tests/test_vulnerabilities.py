from app.vulnerabilities.analyzer import analyze_finding


def test_md5_is_vulnerable():

    finding = {
        "algorithm": "MD5",
        "file": "test.py",
        "line": 10
    }

    result = analyze_finding(
        finding
    )

    assert result["status"] == "Vulnerable"