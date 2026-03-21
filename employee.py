import csv
import os

EMP_FILE = "data/employees.csv"


class Employee:

    def __init__(self, emp_id, name, department, role, joining_date, salary):

        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.role = role
        self.joining_date = joining_date
        self.salary = salary


def initialize_file():

    if not os.path.exists(EMP_FILE):
        with open(EMP_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(
                ["ID", "Name", "Department", "Role", "JoiningDate", "Salary"]
            )


def add_employee():

    emp_id = input("Employee ID: ")
    name = input("Name: ")
    dept = input("Department: ")
    role = input("Role: ")
    join = input("Joining Date (YYYY-MM-DD): ")
    salary = float(input("Base Salary: "))

    with open(EMP_FILE, "a", newline="") as f:

        writer = csv.writer(f)
        writer.writerow([emp_id, name, dept, role, join, salary])

    print("Employee added successfully")


def view_employees():

    with open(EMP_FILE, "r") as f:

        reader = csv.reader(f)

        for row in reader:
            print(row)


def search_employee():

    key = input("Enter Employee Name or ID: ").lower()

    with open(EMP_FILE, "r") as f:

        reader = csv.reader(f)

        for row in reader:

            if key in row[0].lower() or key in row[1].lower():
                print(row)