import cv2
import joblib
from mtcnn import MTCNN
from keras_facenet import FaceNet
import pandas as pd
from datetime import date
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

detector = MTCNN()
embedder = FaceNet()
model, encoder = joblib.load("models/svm_model.pkl")

today = str(date.today())
attendance_file = os.path.join(BASE_DIR, "attendance.csv")

if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Date", "Employee"])
    df.to_csv(attendance_file, index=False)

df = pd.read_csv(attendance_file)

THRESHOLD = 0.60  # confidence threshold

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    try:
        faces = detector.detect_faces(img_rgb)
    except:
        faces = []

    for face in faces:
        x, y, w, h = face['box']
        x, y = max(0, x), max(0, y)

        face_img = img_rgb[y:y+h, x:x+w]
        if face_img.size == 0:
            continue

        face_img = cv2.resize(face_img, (160, 160))
        embedding = embedder.embeddings([face_img])[0]

        probs = model.predict_proba([embedding])[0]
        confidence = max(probs)

        if confidence < THRESHOLD:
            name = "Not Registered"
            color = (0, 0, 255)  # Red
        else:
            pred = model.predict([embedding])
            name = encoder.inverse_transform(pred)[0]
            color = (0, 255, 0)  # Green

            if not ((df["Date"] == today) & (df["Employee"] == name)).any():
                df.loc[len(df)] = [today, name]
                df.to_csv(attendance_file, index=False)

        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
        cv2.putText(frame, name, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Office Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
