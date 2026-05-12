# StudyPulse 📚

A smart and minimal productivity tracker for students to manage study sessions, subjects, marks, and academic performance — built using Flask and designed like a practical B.Tech semester project.

---

## 🚀 Features

### 📖 Subject Management

* Add and organize subjects
* Set target study hours for each subject
* Track subject-wise progress

### ⏱️ Study Session Tracking

* Log daily study sessions
* Record study duration and productivity score
* Maintain consistent study habits

### 📝 Marks & Performance Tracking

* Store exam/test marks
* Calculate percentages automatically
* Monitor academic performance over time

### 📊 Analytics Dashboard

* View total study hours
* Analyze productivity trends
* Identify weak subjects instantly
* Get subject-wise insights

### 📈 Charts & Visualizations

* Auto-generated graphs using Matplotlib
* Study trends and performance analysis
* Clean visual representation of data

### 🎨 Responsive UI

* Modern Bootstrap 5 interface
* Mobile-friendly and easy to use
* Simple and clean student-focused design

---

# 🛠️ Tech Stack

| Category      | Technology              |
| ------------- | ----------------------- |
| Backend       | Flask, Flask-SQLAlchemy |
| Database      | SQLite                  |
| Data Analysis | Pandas, NumPy           |
| Visualization | Matplotlib              |
| Frontend      | Bootstrap 5, HTML, CSS  |

---

# 📂 Project Structure

```bash
StudyPulse/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
│
├── database/
│   └── study_tracker.db       # SQLite database
│
├── static/
│   ├── css/
│   │   └── style.css          # Custom styles
│   ├── js/                    # JavaScript files
│   └── charts/                # Generated chart images
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   ├── subjects.html
│   ├── sessions.html
│   ├── marks.html
│   ├── analytics.html
│   ├── add_subject.html
│   ├── add_session.html
│   └── add_mark.html
│
├── modules/
│   ├── database_manager.py    # Database operations
│   ├── analytics.py           # Analytics functions
│   ├── chart_generator.py     # Graph generation
│   ├── validators.py          # Input validation
│   └── utilities.py           # Helper utilities
│
├── models/
│   ├── subject.py             # Subject model
│   ├── session.py             # StudySession model
│   └── marks.py               # Marks model
│
└── exports/                   # Exported reports/data
```

---

# ⚙️ Setup & Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Aradhy777/Study-Plus.git
cd StudyPulse
```

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run the Application

```bash
python app.py
```

The application will run locally at:

```bash
http://localhost:5000
```

---

# 📌 How to Use

### ➕ Add Subjects

Create subjects and define target study hours.

### 📚 Log Study Sessions

Track your daily study duration and productivity level.

### 📝 Add Marks

Store marks for tests/exams and monitor percentages.

### 📊 View Dashboard & Analytics

Analyze study performance through statistics and charts.

---

# 🔍 Core Functionalities

## 📋 Dashboard

* Total study hours
* Average productivity score
* Subject-wise study analysis
* Weak subject detection

## 📈 Analytics

* Daily/weekly study trends
* Marks performance graphs
* Productivity growth tracking
* Auto-generated charts using Matplotlib

## 🗂️ Data Management

* Add/Delete subjects
* Add/Delete sessions
* Add/Delete marks
* Automatic real-time calculations

---

# ☁️ Deployment Options

You can deploy this project on:

* Railway
* PythonAnywhere
* Heroku
* AWS EC2
* DigitalOcean

---

# 📌 Additional Notes

* Uses SQLite for local database storage
* Charts regenerate dynamically on analytics requests
* Single-user application (No authentication system)
* Fully responsive for desktop and mobile devices

---

# 🎓 About the Project

StudyPulse is designed as a practical academic productivity tracker inspired by real student workflows.
The project focuses on learning Flask development, database handling, analytics, and frontend integration in a simple and structured way.

---

# 📄 License

This project is open-source and intended for educational and learning purposes.
