def build_chat_context(
    question: str,
    security_data: dict
) -> dict:

    return {
        "question": question,
        "security_data": security_data
    }