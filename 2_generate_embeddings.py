from mtcnn import MTCNN
from keras_facenet import FaceNet
import cv2
import os
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dataset_dir = os.path.join(BASE_DIR, "dataset")

detector = MTCNN()
embedder = FaceNet()

X, y = [], []
MIN_FACE_SIZE = 50

for person in os.listdir(dataset_dir):
    person_path = os.path.join(dataset_dir, person)

    for img_name in os.listdir(person_path):
        img_path = os.path.join(person_path, img_name)
        img = cv2.imread(img_path)

        if img is None or img.shape[0] < 100 or img.shape[1] < 100:
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        try:
            faces = detector.detect_faces(img_rgb)
        except:
            continue

        for face_data in faces:
            x, y_, w, h = face_data['box']
            x, y_ = max(0, x), max(0, y_)
            w, h = abs(w), abs(h)

            if w < MIN_FACE_SIZE or h < MIN_FACE_SIZE:
                continue

            face = img_rgb[y_:y_+h, x:x+w]
            if face.size == 0:
                continue

            face = cv2.resize(face, (160, 160))
            embedding = embedder.embeddings([face])[0]

            X.append(embedding)
            y.append(person)

os.makedirs("embeddings", exist_ok=True)
np.savez("embeddings/faces_embeddings.npz", X=np.array(X), y=np.array(y))

print("✅ Face embeddings generated successfully")
print("Total samples:", len(X))
