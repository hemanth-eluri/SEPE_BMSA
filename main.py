from employee import *
from performance import *
from bonus import *
from analytics import *

initialize_file()

while True:

    print("\nSMART EMPLOYEE PERFORMANCE SYSTEM")

    print("1 Add Employee")
    print("2 View Employees")
    print("3 Search Employee")

    print("4 Add Performance")
    print("5 View Performance")

    print("6 Calculate Bonus")

    print("7 Department Performance Chart")
    print("8 Bonus Distribution Chart")

    print("9 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        add_performance()

    elif choice == "5":
        view_performance()

    elif choice == "6":
        calculate_bonus()

    elif choice == "7":
        department_performance()

    elif choice == "8":
        bonus_distribution()

    elif choice == "9":
        break

    else:
        print("Invalid choice")