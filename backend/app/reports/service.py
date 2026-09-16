import os

from .json import create_json_report
from .txt import create_txt_report
from .pdf import create_pdf_report


REPORT_DIRECTORY = "storage/generated_reports"


def generate_report(
    cbom: dict,
    report_format: str,
    project_id: int
):

    os.makedirs(
        REPORT_DIRECTORY,
        exist_ok=True
    )

    filename = (
        f"project_{project_id}"
        f"_security_report"
    )

    if report_format == "json":

        content = create_json_report(
            cbom
        )

        path = os.path.join(
            REPORT_DIRECTORY,
            filename + ".json"
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return path

    if report_format == "txt":

        content = create_txt_report(
            cbom
        )

        path = os.path.join(
            REPORT_DIRECTORY,
            filename + ".txt"
        )

        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return path

    if report_format == "pdf":

        path = os.path.join(
            REPORT_DIRECTORY,
            filename + ".pdf"
        )

        create_pdf_report(
            cbom,
            path
        )

        return path

    raise ValueError(
        "Unsupported report format"
    )