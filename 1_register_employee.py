import cv2
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_dir = os.path.join(BASE_DIR, "dataset")
os.makedirs(dataset_dir, exist_ok=True)

emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")

folder_name = f"{emp_id}_{name}"
person_path = os.path.join(dataset_dir, folder_name)
os.makedirs(person_path, exist_ok=True)

details_file = os.path.join(BASE_DIR, "employee_details.csv")
if not os.path.exists(details_file):
    df = pd.DataFrame(columns=["EmployeeID", "Name"])
    df.to_csv(details_file, index=False)

df = pd.read_csv(details_file)
df.loc[len(df)] = [emp_id, name]
df.to_csv(details_file, index=False)

cap = cv2.VideoCapture(0)
count = 0

print("Press 'S' to save image | 'Q' to quit")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Register Employee", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite(os.path.join(person_path, f"{count}.jpg"), frame)
        count += 1
        print("Saved image", count)
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
