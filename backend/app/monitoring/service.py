from .security_trends import calculate_security_trends


def get_security_monitoring(
    scan_history: list
) -> dict:

    trends = calculate_security_trends(
        scan_history
    )

    return {
        "monitoring": trends
    }