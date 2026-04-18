from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(df, filename="report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Climate Analysis Report", styles['Title']))

    avg_temp = df['Temperature'].mean()
    avg_co2 = df['CO2'].mean()

    content.append(Paragraph(f"Average Temperature: {avg_temp:.2f}", styles['Normal']))
    content.append(Paragraph(f"Average CO2: {avg_co2:.2f}", styles['Normal']))

    doc.build(content)