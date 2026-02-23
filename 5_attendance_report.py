import pandas as pd

attendance = pd.read_csv("attendance.csv")
employees = pd.read_csv("employee_details.csv")

total_days = attendance["Date"].nunique()

print("\n--- Attendance Report ---\n")

for _, row in employees.iterrows():
    emp_key = row["EmployeeID"] + "_" + row["Name"]
    present = attendance[attendance["Employee"] == emp_key]["Date"].nunique()
    leave = total_days - present

    print("Employee:", row["Name"])
    print("Present Days:", present)
    print("Leave Days:", leave)
    print("-------------------------")
