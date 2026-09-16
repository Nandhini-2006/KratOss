from .mapper import create_attack_surface


def generate_attack_surface(analysis_result):
    vulnerabilities = analysis_result.get(
        "vulnerabilities",
        []
    )

    attack_surface = create_attack_surface(
        vulnerabilities
    )

    return {
        "project_id": analysis_result["project_id"],
        "attack_surface": attack_surface
    }