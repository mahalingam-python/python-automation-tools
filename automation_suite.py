import os
import json
from datetime import datetime

print("=" * 60)
print("         PYTHON AUTOMATION TOOLS")
print("=" * 60)

tasks = [
    "Create Project Folder",
    "Generate Report",
    "Save JSON Data",
    "Create Log File",
    "Verify Files"
]

folder = "automation_output"

if not os.path.exists(folder):
    os.makedirs(folder)
    print("Project folder created.")
else:
    print("Project folder already exists.")

report = os.path.join(folder, "report.txt")

with open(report, "w", encoding="utf-8") as file:
    file.write("Automation Report\n")
    file.write("=" * 40 + "\n")
    file.write(f"Generated: {datetime.now()}\n\n")

    for index, task in enumerate(tasks, start=1):
        file.write(f"{index}. {task}\n")

print("Report generated successfully.")

data = {
    "project": "Python Automation Tools",
    "tasks": tasks,
    "status": "Completed",
    "generated_at": str(datetime.now())
}

json_file = os.path.join(folder, "summary.json")

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("JSON summary created.")

log_file = os.path.join(folder, "automation.log")

with open(log_file, "w", encoding="utf-8") as file:
    file.write("Automation Log\n")
    file.write(f"Created: {datetime.now()}\n")
    file.write("Status: Success\n")

print("Log file generated.")

print("\nVerification")
print("-" * 60)

files = [report, json_file, log_file]

for file in files:
    if os.path.exists(file):
        print(f"[OK] {file}")
    else:
        print(f"[FAILED] {file}")

print("\nAutomation completed successfully.")
print("=" * 60)
