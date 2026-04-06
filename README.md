# 🧑‍💻 Face Recognition Attendance System

An **AI-powered Attendance Management System** that uses **face recognition technology** to automatically mark employee attendance.

This system captures facial data, generates embeddings, trains a recognition model, and records attendance in real-time with reports.

---

## 🚀 Features

* 👤 Employee Registration with face capture
* 🧠 Face embedding generation
* 🤖 Model training for recognition
* 📸 Real-time face detection & attendance marking
* 📊 Attendance report generation (CSV)
* ⚡ Fast and automated workflow
* 🗂️ Organized dataset and model storage

---

## 🧠 Technologies Used

* **Python**
* **OpenCV**
* **Face Recognition / Embeddings**
* **NumPy**
* **Pandas**

---

## 📂 Project Structure

```id="stru293"
Face-Recognition-Attendance-System/
│
├── dataset/                      # Stored face images
├── embeddings/                  # Face embeddings
├── models/                      # Trained models
│
├── 1_register_employee.py       # Capture employee images
├── 2_generate_embeddings.py     # Create facial embeddings
├── 3_train_model.py             # Train recognition model
├── 4_mark_attendance.py         # Mark attendance
├── 5_attendance_report.py       # Generate reports
│
├── employee_details.csv         # Employee data
├── attendance.csv               # Attendance records
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```id="clone123"
git clone https://github.com/your-username/face-recognition-attendance-system.git
cd face-recognition-attendance-system
```

### 2️⃣ Install Dependencies

```id="install456"
pip install -r requirements.txt
```

### 3️⃣ Run Modules (Step-by-Step)

#### ▶️ Register Employee

```id="run1"
python 1_register_employee.py
```

#### ▶️ Generate Embeddings

```id="run2"
python 2_generate_embeddings.py
```

#### ▶️ Train Model

```id="run3"
python 3_train_model.py
```

#### ▶️ Mark Attendance

```id="run4"
python 4_mark_attendance.py
```

#### ▶️ Generate Report

```id="run5"
python 5_attendance_report.py
```

---

## 🎮 How It Works

1. Register employee faces via webcam
2. Store images in dataset
3. Convert images into embeddings
4. Train recognition model
5. Detect faces in real-time
6. Mark attendance automatically
7. Generate attendance reports

---

## 📊 Output

* ✅ Attendance stored in CSV file
* 📈 Reports generated for analysis
* 🧑‍💼 Employee-wise tracking

---

## 🎯 Applications

* 🏢 Office attendance systems
* 🎓 College attendance automation
* 🏭 Industrial workforce tracking
* 🔐 Secure access systems

---

## 🔮 Future Enhancements

* 🌐 Web dashboard (Flask/Streamlit)
* 📱 Mobile app integration
* 🧠 Deep learning-based recognition
* ☁️ Cloud database integration
* 🔔 Real-time notifications

---

## 🙌 Acknowledgements

* OpenCV Library
* Python Community
* Face Recognition Models

---

## 📌 Author

**Navodaya**
💻 Aspiring AI/ML Developer

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
