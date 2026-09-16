from .chat import build_chat_context
from .explainer import build_explanation_context
from .fix_advisor import build_fix_advisor_context


def prepare_chat(
    question: str,
    security_data: dict
):

    return build_chat_context(
        question,
        security_data
    )


def prepare_explanation(
    vulnerability: dict
):

    return build_explanation_context(
        vulnerability
    )


def prepare_fix_advice(
    vulnerability: dict,
    code: str = ""
):

    return build_fix_advisor_context(
        vulnerability,
        code
    )