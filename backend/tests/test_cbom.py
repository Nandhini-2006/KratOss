from app.cbom.validator import validate_cbom


def test_cbom_validation():

    cbom = {
        "cbom_version": "1.0",
        "generated_at": "2026-01-01",
        "project_id": 1,
        "summary": {},
        "crypto_assets": []
    }

    result = validate_cbom(
        cbom
    )

    assert result["valid"] is True