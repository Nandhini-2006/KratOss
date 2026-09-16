REQUIRED_FIELDS = [
    "cbom_version",
    "generated_at",
    "project_id",
    "summary",
    "crypto_assets"
]


def validate_cbom(cbom: dict) -> dict:

    missing_fields = []

    for field in REQUIRED_FIELDS:

        if field not in cbom:
            missing_fields.append(field)

    if missing_fields:

        return {
            "valid": False,
            "missing_fields": missing_fields
        }

    if not isinstance(
        cbom["crypto_assets"],
        list
    ):

        return {
            "valid": False,
            "missing_fields": [],
            "error": "crypto_assets must be a list"
        }

    return {
        "valid": True,
        "missing_fields": []
    }