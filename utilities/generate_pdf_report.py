import os
import glob
import json

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

tester = os.getenv("GITHUB_ACTOR", "Lubabalo Mkhize")

browser = os.getenv("BROWSER", "Edge")

environment = os.getenv("TEST_ENV", "QA")

execution_date = datetime.now().strftime("%d %B %Y %H:%M:%S")

repository = os.getenv("GITHUB_REPOSITORY", "Local Execution")

branch = os.getenv("GITHUB_REF_NAME", "main")

run_number = os.getenv("GITHUB_RUN_NUMBER", "N/A")

commit = os.getenv("GITHUB_SHA", "N/A")[:7]


# =====================================================
# Read Allure Results
# =====================================================

passed = 0
failed = 0
skipped = 0

start_times = []
stop_times = []

result_files = glob.glob("allure-results/*-result.json")

for file in result_files:

    with open(file, encoding="utf-8") as f:
        result = json.load(f)

    status = result.get("status")

    if status == "passed":
        passed += 1

    elif status == "failed":
        failed += 1

    elif status == "skipped":
        skipped += 1

    if "start" in result:
        start_times.append(result["start"])

    if "stop" in result:
        stop_times.append(result["stop"])

total_tests = passed + failed + skipped

if total_tests > 0:
    pass_rate = round((passed / total_tests) * 100, 2)
else:
    pass_rate = 0

if start_times and stop_times:
    execution_time = round((max(stop_times) - min(start_times)) / 1000, 2)
else:
    execution_time = 0

status = "PASSED"

if failed > 0:
    status = "FAILED"

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

    ["Repository", repository],

    ["Branch", branch],

    ["Run Number", run_number],

    ["Commit", commit],

    ["Execution Time", f"{execution_time} sec"],

    ["Total Tests", str(total_tests)],

    ["Passed", str(passed)],

    ["Failed", str(failed)],

    ["Skipped", str(skipped)],

    ["Pass Rate", f"{pass_rate}%"],

    ["Overall Status", status]

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

This report was generated automatically after the execution of the
<b>{project_name}</b> automation suite.

<b>Total Tests Executed:</b> {total_tests}<br/>
<b>Passed:</b> {passed}<br/>
<b>Failed:</b> {failed}<br/>
<b>Skipped:</b> {skipped}<br/>
<b>Pass Rate:</b> {pass_rate}%<br/>
<b>Execution Time:</b> {execution_time} seconds<br/><br/>

<b>Environment:</b> {environment}<br/>
<b>Browser:</b> {browser}<br/>
<b>Repository:</b> {repository}<br/>
<b>Branch:</b> {branch}<br/>
<b>Run Number:</b> {run_number}<br/>

Overall execution status:
<b>{status}</b>
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