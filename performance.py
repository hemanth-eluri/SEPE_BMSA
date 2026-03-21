import csv

PERF_FILE = "data/performance.csv"


def add_performance():

    emp_id = input("Employee ID: ")

    attendance = float(input("Attendance Score (0-100): "))
    tasks = float(input("Task Completion Score: "))
    project = float(input("Project Contribution Score: "))
    feedback = float(input("Manager Feedback Score: "))

    score = calculate_score(attendance, tasks, project, feedback)

    with open(PERF_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(
            [emp_id, attendance, tasks, project, feedback, score]
        )

    print("Performance recorded")


def calculate_score(att, task, proj, feed):

    score = (att * 0.2) + (task * 0.3) + (proj * 0.3) + (feed * 0.2)

    return round(score, 2)


def classify_performance(score):

    if score >= 85:
        return "Excellent"

    elif score >= 70:
        return "Good"

    elif score >= 50:
        return "Average"

    else:
        return "Needs Improvement"


def view_performance():

    with open(PERF_FILE, "r") as f:

        reader = csv.reader(f)

        for row in reader:

            score = float(row[5])
            level = classify_performance(score)

            print(row, "Performance:", level)