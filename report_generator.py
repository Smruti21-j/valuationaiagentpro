
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from io import BytesIO

def generate_pdf_report(result, client_name, valuation_date, wacc, terminal_growth, projection_years):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40)
    styles = getSampleStyleSheet()
    styleH = styles["Heading1"]
    styleN = styles["BodyText"]
    story = []

    story.append(Paragraph("Valuation Report", styleH))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Client: {client_name}", styleN))
    story.append(Paragraph(f"Valuation Date: {valuation_date}", styleN))
    story.append(Paragraph("Prepared by: ValServe Corporate Advisors LLP", styleN))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Executive Summary", styleH))
    story.append(Paragraph(f"The estimated equity value using DCF is ₹{result['Total Valuation']} Lakhs.", styleN))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Valuation Methodology", styleH))
    story.append(Paragraph(f"Method: DCF<br/>WACC: {wacc}%<br/>Terminal Growth: {terminal_growth}%<br/>Projection Period: {projection_years} years", styleN))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Valuation Summary", styleH))
    story.append(Paragraph(f"NPV of Cash Flows: ₹{result['NPV']} Lakhs", styleN))
    story.append(Paragraph(f"Terminal Value (PV): ₹{result['Terminal Value PV']} Lakhs", styleN))
    story.append(Paragraph(f"Total Valuation: ₹{result['Total Valuation']} Lakhs", styleN))

    story.append(PageBreak())

    story.append(Paragraph("Scope & Limitations", styleH))
    story.append(Paragraph("This report is prepared solely for internal use and should not be distributed externally. It is based on assumptions and data provided by management.", styleN))

    doc.build(story)
    buffer.seek(0)
    return buffer
