# 🏆 Sports Track - Sports Attendance Management System

## 📌 Project Overview

Sports Track is a web-based Sports Attendance Management System developed as a third-year college project. The system helps educational institutions manage student sports participation, attendance, and approval workflows efficiently. It digitizes the traditional attendance process and provides role-based access for different users.

---

## 🎯 Objectives

- Digitize sports attendance management.
- Reduce manual paperwork.
- Track student participation in sports activities.
- Manage attendance approval through different authority levels.
- Generate attendance records efficiently.

---

## ✨ Features

- 🔐 User Authentication and Login
- 👨‍🎓 Student Management
- 👨‍🏫 Teacher Management
- 🏫 Department Management
- 🥋 Sports Event Management
- ✅ Attendance Marking
- 📋 Attendance Approval Workflow
- 📊 Attendance Reports
- 🔍 Search and Filter Records
- 📅 Event Scheduling

---

## 👥 User Roles

- Principal
- Head of Department (HOD)
- Tutor
- Physical Education Teacher
- Student

Each user has different permissions based on their role.

---

## 🔄 Attendance Workflow

Teacher → Tutor → HOD → Principal

Attendance submitted by the Physical Education Teacher passes through the approval process before becoming final.

---

## 🏅 Supported Sports

- Football
- Kho-Kho
- Taekwondo
- Athletics
- Other college sports events

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Bootstrap
- JavaScript

### Backend
- Python
- Django

### Database
- SQLite

---

## 📂 Project Structure

```
SportsTrack/
│
├── accounts/
├── attendance/
├── events/
├── students/
├── teachers/
├── templates/
├── static/
├── media/
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/SportsTrack.git
```

### Move to Project Directory

```bash
cd SportsTrack
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

Open your browser and visit

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

You can add screenshots here.

- Login Page
- Dashboard
- Student Management
- Attendance Page
- Reports

---

## 📈 Future Enhancements

- QR Code Attendance
- Face Recognition Attendance
- Mobile Application
- Email Notifications
- SMS Alerts
- Data Analytics Dashboard
- Cloud Database Support

---

## 🎓 Academic Information

**Project Title:** Sports Track - Sports Attendance Management System

**Project Type:** Third Year College Mini Project

**Course:** Integrated M.Sc Computer Science (AI & ML)

---

## 👨‍💻 Author

**Arjun M**

Integrated M.Sc Computer Science (AI & ML)

---

## 📜 License

This project is developed for educational purposes only.

---

## ⭐ Acknowledgement

We sincerely thank our faculty members and our college for their valuable guidance and support throughout the development of this project.
