from app.reports.json import create_json_report


def test_json_report():

    cbom = {
        "project_id": 1,
        "crypto_assets": []
    }

    result = create_json_report(
        cbom
    )

    assert isinstance(
        result,
        str
    )