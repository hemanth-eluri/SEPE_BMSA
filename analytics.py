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

    df = pd.read_csv(BONUS_FILE)

    total = df["Bonus"].sum()

    labels = df["Name"]

    plt.pie(df["Bonus"], labels=labels, autopct="%1.1f%%")

    plt.title("Bonus Distribution")

    plt.show()