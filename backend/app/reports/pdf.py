from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def create_pdf_report(
    cbom: dict,
    output_path: str
):

    document = SimpleDocTemplate(
        output_path,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "KRATOS - Cryptographic Security Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Project ID: {cbom.get('project_id')}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"CBOM Version: {cbom.get('cbom_version')}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 20))

    summary = cbom.get("summary", {})

    data = [
        ["Metric", "Value"],
        [
            "Crypto Assets",
            summary.get("total_crypto_assets", 0)
        ],
        [
            "Vulnerabilities",
            summary.get("total_vulnerabilities", 0)
        ],
        [
            "Quantum Findings",
            summary.get("total_quantum_findings", 0)
        ]
    ]

    table = Table(data)

    table.setStyle(
        TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("PADDING", (0, 0), (-1, -1), 6)
        ])
    )

    story.append(table)

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "Cryptographic Assets",
            styles["Heading2"]
        )
    )

    for asset in cbom.get(
        "crypto_assets",
        []
    ):

        vulnerability = asset.get(
            "vulnerability",
            {}
        )

        quantum = asset.get(
            "quantum_security",
            {}
        )

        text = (
            f"<b>Algorithm:</b> "
            f"{asset.get('algorithm')}<br/>"
            f"<b>File:</b> "
            f"{asset.get('file')}<br/>"
            f"<b>Line:</b> "
            f"{asset.get('line')}<br/>"
            f"<b>Status:</b> "
            f"{vulnerability.get('status')}<br/>"
            f"<b>Risk:</b> "
            f"{vulnerability.get('risk_level')}<br/>"
            f"<b>Quantum Risk:</b> "
            f"{quantum.get('risk')}<br/>"
            f"<b>Mosca Risk:</b> "
            f"{quantum.get('mosca_risk', {}).get('risk')}"
        )

        story.append(
            Paragraph(
                text,
                styles["Normal"]
            )
        )

        story.append(
            Spacer(1, 12)
        )

    document.build(story)