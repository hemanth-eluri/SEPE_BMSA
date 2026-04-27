import csv
from datetime import datetime

EMP_FILE = "data/employees.csv"
PERF_FILE = "data/performance.csv"
BONUS_FILE = "data/bonus_report.csv"


def calculate_bonus():

    employees = {}
    performance = {}

    with open(EMP_FILE) as f:

        reader = csv.DictReader(f)

        for row in reader:
            employees[row["ID"]] = row

    with open(PERF_FILE) as f:

        reader = csv.reader(f)

        for row in reader:
            performance[row[0]] = float(row[5])

    with open(BONUS_FILE, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(["ID", "Name", "Score", "Bonus"])

        for emp_id in performance:

            score = performance[emp_id]

            # Check if employee exists before calculating bonus
            if emp_id in employees:
                salary = float(employees[emp_id]["Salary"])

                bonus = determine_bonus(score, salary)

                writer.writerow(
                    [emp_id, employees[emp_id]["Name"], score, bonus]
                )

    print("Bonus report generated")


def determine_bonus(score, salary):

    if score >= 85:
        return salary * 0.20

    elif score >= 70:
        return salary * 0.10

    elif score >= 50:
        return salary * 0.05

    else:
        return 0