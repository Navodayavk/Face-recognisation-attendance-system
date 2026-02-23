import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import joblib
import os

data = np.load("embeddings/faces_embeddings.npz")
X, y = data["X"], data["y"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

model = SVC(kernel="linear", probability=True)
model.fit(X, y_encoded)

os.makedirs("models", exist_ok=True)
joblib.dump((model, encoder), "models/svm_model.pkl")

print("✅ Face recognition model trained and saved")
