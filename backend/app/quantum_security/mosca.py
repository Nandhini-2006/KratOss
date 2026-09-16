def calculate_mosca_risk(
    data_lifetime_years: int,
    migration_time_years: int,
    quantum_arrival_years: int
) -> dict:

    total_required_time = (
        data_lifetime_years +
        migration_time_years
    )

    if total_required_time >= quantum_arrival_years:
        risk = "HIGH"

    elif total_required_time >= quantum_arrival_years * 0.7:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    return {
        "data_lifetime_years": data_lifetime_years,
        "migration_time_years": migration_time_years,
        "quantum_arrival_years": quantum_arrival_years,
        "total_required_time": total_required_time,
        "risk": risk
    }