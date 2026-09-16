import json


def create_json_report(cbom: dict) -> str:

    return json.dumps(
        cbom,
        indent=4,
        default=str
    )