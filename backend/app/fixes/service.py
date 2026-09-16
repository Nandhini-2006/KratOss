from .fix_suggestions import build_fix_context


def prepare_fix(
    vulnerability: dict
) -> dict:

    context = build_fix_context(
        vulnerability
    )

    return {
        "vulnerability": vulnerability,
        "ai_context": context
    }


def prepare_multiple_fixes(
    vulnerabilities: list
) -> list:

    results = []

    for vulnerability in vulnerabilities:

        results.append(
            prepare_fix(vulnerability)
        )

    return results