# Automated Waste Detection & Segregation System

An intelligent waste classification and segregation system powered by **YOLOv8**, **OpenCV**, and **Django**, integrated with **Firebase Realtime Database** for automated mechanical sorting.

---

## 📌 Features

- **Real-Time Object Detection**: Detects and classifies waste items into categories such as **Biodegradable** and **Non-Biodegradable** with high frame rates using YOLOv8 Nano.
- **Web Dashboard**: A Django-based management portal to trigger detection sessions, inspect historical records, and manage user accounts.
- **Firebase IoT Integration**: Synchronizes real-time prediction signals to Firebase Realtime Database to command conveyor/sorter hardware (Branch A vs. Branch B).
- **Persistent Logging**: Stores detection timestamps, confidence levels, and bounding box coordinates into a local SQLite database and Excel logs.

---

## 📂 Repository Structure

```
├── data.yaml                          # YOLOv8 dataset configuration
├── model.py                           # Model training script
├── final.py                           # Standalone OpenCV webcam inference script
├── test/                              # Sample evaluation images and labels
├── runs/                              # Training runs and performance metrics
└── DEPLOYMENT/
    └── PROJECT/                       # Django Web Application
        ├── manage.py
        ├── PROJECT/                   # Settings & root routing
        └── APP/                       # Core Django app
            ├── bio.pt                 # Trained YOLOv8 model weights
            ├── models.py              # Database models (Detected, UserPersonalModel)
            ├── views.py               # Detection and database views
            └── static/                # CSS, JavaScript, and asset libraries
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+
- Git

### 2. Installation

Clone the repository and install required packages:

```bash
git clone https://github.com/Butteryjam/waste-detection.git
cd waste-detection
pip install -r requirements.txt
```

*(Or install core dependencies directly)*:
```bash
pip install ultralytics opencv-python cvzone django firebase-admin openpyxl pygame
```

### 3. Running Standalone Inference
To run real-time waste classification from your webcam:
```bash
python final.py
```

### 4. Running the Web Application
```bash
cd DEPLOYMENT/PROJECT
python manage.py migrate
python manage.py runserver
```

---

## 🔒 Configuration & Security

- Place your Firebase Admin SDK service account key inside `DEPLOYMENT/PROJECT/APP/` and ensure your database URL in `views.py` matches your Firebase configuration.
- Sensitive files (`*-firebase-adminsdk-*.json`, `db.sqlite3`) are excluded from version control via `.gitignore`.
