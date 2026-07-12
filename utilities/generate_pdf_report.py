import os
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

# ============================================
# Test Execution Data
# Replace these with values from your framework
# ============================================

project_name = "Sauce Demo Automation"
framework = "Selenium Python + Pytest"
tester = "Lubabalo Mkhize"
browser = os.getenv("BROWSER", "Edge")
environment = "QA"

total_tests = 3
passed = 2
failed = 1
skipped = 0

execution_date = datetime.now().strftime("%d %B %Y %H:%M")

pass_rate = round((passed / total_tests) * 100, 2)

status = "PASSED"

if failed > 0:
    status = "FAILED"

# ============================================

os.makedirs("reports", exist_ok=True)

pdf_file = "reports/TestExecutionReport.pdf"

doc = SimpleDocTemplate(pdf_file)

styles = getSampleStyleSheet()

story = []

# ============================================
# Title
# ============================================

title = Paragraph(
    "<b><font size=18>Automation Test Execution Summary</font></b>",
    styles["Title"]
)

story.append(title)
story.append(Spacer(1, 20))

# ============================================
# Summary Table
# ============================================

data = [

    ["Project", project_name],

    ["Framework", framework],

    ["Tester", tester],

    ["Browser", browser],

    ["Environment", environment],

    ["Execution Date", execution_date],

    ["Total Tests", str(total_tests)],

    ["Passed", str(passed)],

    ["Failed", str(failed)],

    ["Skipped", str(skipped)],

    ["Pass Rate", f"{pass_rate}%"],

    ["Overall Status", status],

]

table = Table(data, colWidths=[170, 250])

table.setStyle(TableStyle([

    ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),

    ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),

    ("GRID", (0, 0), (-1, -1), 1, colors.grey),

    ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),

    ("FONTSIZE", (0, 0), (-1, -1), 11),

    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

]))

story.append(table)

story.append(Spacer(1, 30))

# ============================================
# Executive Summary
# ============================================

summary = f"""
<b>Execution Summary</b><br/><br/>

A total of <b>{total_tests}</b> automated test cases were executed.

<b>{passed}</b> passed successfully,
<b>{failed}</b> failed,
and <b>{skipped}</b> were skipped.

Overall execution completed with a
<b>{pass_rate}%</b> pass rate.

Environment tested:
<b>{environment}</b>

Browser used:
<b>{browser}</b>

Framework:
<b>{framework}</b>
"""

story.append(Paragraph(summary, styles["BodyText"]))

story.append(Spacer(1, 20))

# ============================================
# Footer
# ============================================

footer = Paragraph(
    "<font size=9 color='grey'>Generated automatically by GitHub Actions CI/CD Pipeline</font>",
    styles["Normal"]
)

story.append(footer)

doc.build(story)

print("PDF report generated successfully.")