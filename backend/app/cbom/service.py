from .generator import generate_cbom
from .validator import validate_cbom


def create_cbom(
    scan_result: dict,
    vulnerability_result: dict,
    quantum_result: dict
) -> dict:

    cbom = generate_cbom(
        scan_result,
        vulnerability_result,
        quantum_result
    )

    validation = validate_cbom(
        cbom
    )

    if not validation["valid"]:

        return {
            "valid": False,
            "validation": validation
        }

    return {
        "valid": True,
        "validation": validation,
        "cbom": cbom
    }