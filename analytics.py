import pandas as pd
import matplotlib.pyplot as plt

EMP_FILE = "data/employees.csv"
PERF_FILE = "data/performance.csv"
BONUS_FILE = "data/bonus_report.csv"


def department_performance():

    emp = pd.read_csv(EMP_FILE)
    perf = pd.read_csv(PERF_FILE)

    perf.columns = ["ID","Attendance","Tasks","Project","Feedback","Score"]

    df = pd.merge(emp, perf, left_on="ID", right_on="ID")

    avg = df.groupby("Department")["Score"].mean()

    print(avg)

    avg.plot(kind="bar")

    plt.title("Department Average Performance")

    plt.show()


def bonus_distribution():

    import os
    
    if not os.path.exists(BONUS_FILE) or os.path.getsize(BONUS_FILE) == 0:
        print("No bonus report available. Generate bonus report first.")
        return
    
    df = pd.read_csv(BONUS_FILE)

    if df.empty or len(df) < 2:
        print("Not enough data for bonus distribution chart.")
        return

    labels = df["Name"]

    plt.figure(figsize=(10, 6))
    plt.pie(df["Bonus"], labels=labels, autopct="%1.1f%%", startangle=90)

    plt.title("Bonus Distribution")

    plt.show()