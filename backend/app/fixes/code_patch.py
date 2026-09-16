def create_patch(
    file_content: str,
    old_code: str,
    new_code: str
) -> dict:

    if old_code not in file_content:

        return {
            "success": False,
            "message": "Original code was not found"
        }

    updated_content = file_content.replace(
        old_code,
        new_code,
        1
    )

    return {
        "success": True,
        "old_code": old_code,
        "new_code": new_code,
        "updated_content": updated_content
    }