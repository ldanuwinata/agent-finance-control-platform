from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


class ReportAgent:
    """
    Generates an audit-style PDF report for portfolio exceptions.
    """

    def export_pdf(self, exceptions, analyses, output_file):

        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        document = SimpleDocTemplate(str(output_path))
        styles = getSampleStyleSheet()

        story = []

        # -------------------------------------------------
        # Title
        # -------------------------------------------------

        story.append(
            Paragraph("<b>Agentic Finance Control Platform</b>", styles["Title"])
        )

        story.append(
            Paragraph("Portfolio Exception Report", styles["Heading2"])
        )

        story.append(Spacer(1, 20))

        # -------------------------------------------------
        # Summary
        # -------------------------------------------------

        story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))

        story.append(
            Paragraph(
                f"Exceptions detected: {len(exceptions)}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        # -------------------------------------------------
        # Exception Details
        # -------------------------------------------------

        for i, (_, row) in enumerate(exceptions.iterrows(), start=1):

            story.append(
                Paragraph(
                    f"<b>Exception #{i}</b>",
                    styles["Heading2"]
                )
            )

            story.append(
                Paragraph(f"<b>Fund:</b> {row['Fund']}", styles["Normal"])
            )

            story.append(
                Paragraph(f"<b>ISIN:</b> {row['ISIN']}", styles["Normal"])
            )

            story.append(
                Paragraph(
                    f"<b>Number of Shares:</b> {row['NumberOfShares']}",
                    styles["Normal"]
                )
            )

            story.append(
                Paragraph(
                    f"<b>Market Value:</b> {row['MarketValue']}",
                    styles["Normal"]
                )
            )

            story.append(
                Paragraph(
                    f"<b>Currency:</b> {row['Currency']}",
                    styles["Normal"]
                )
            )

            story.append(
                Paragraph(
                    f"<b>Exception:</b> {row['ExceptionType']}",
                    styles["Normal"]
                )
            )

            story.append(
                Paragraph(
                    f"<b>AI Assessment:</b> {analyses[i-1]['Analysis']}",
                    styles["Normal"]
                )
            )

            story.append(Spacer(1, 20))

        document.build(story)

        print(f"✅ PDF report created: {output_path}")