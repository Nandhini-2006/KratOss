from app.quantum_security.quantum_risk import (
    check_quantum_risk
)


def test_rsa_quantum_risk():

    result = check_quantum_risk(
        "RSA"
    )

    assert result["quantum_sensitive"] is True
    assert result["risk"] == "HIGH"