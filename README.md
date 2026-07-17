# 🚨 ResQAI - AI Powered Disaster Response & Rescue Management System

## 📌 Overview

ResQAI is a Flask-based disaster response backend developed during a hackathon. It helps victims send SOS requests, enables rescue teams to manage emergencies, and allows administrators to monitor shelters and rescue operations.

The system uses JWT authentication, role-based access control, and MySQL for secure and efficient disaster management.

---

## 🚀 Features

### 👤 Authentication
- User Registration
- User Login
- JWT Authentication
- Role-Based Authorization
  - Admin
  - Victim
  - Rescue Team

### 🆘 SOS Module
- Create SOS Request
- View SOS Requests
- Update SOS Status
- Delete SOS Request

### 🏠 Shelter Module
- Add Shelter
- View Shelters
- Update Shelter Details
- Delete Shelter

### 🚑 Rescue Module
- Create Rescue Teams
- View Pending SOS Requests
- Update Rescue Status
- Assign Rescue Teams

### 👨‍💼 Admin Module
- Manage Users
- Manage Shelters
- Monitor Rescue Operations
- Dashboard APIs

---

## 🛠️ Tech Stack

### Backend
- Python
- Flask
- Flask-JWT-Extended
- SQLAlchemy

### Database
- MySQL

### API Testing
- Thunder Client

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```
ResQAI
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
│
├── models
├── routes
├── utils
│
└── README.md
```

---

## 🔐 Authentication

The project uses JWT Tokens for secure API access.

Example Header

```
Authorization: Bearer <JWT_TOKEN>
```

---

## 📡 API Modules

### Authentication

- POST /auth/register
- POST /auth/login

### SOS

- POST /sos/create
- GET /sos/all
- GET /sos/<id>
- PUT /sos/update/<id>
- DELETE /sos/delete/<id>

### Shelter

- POST /shelter/create
- GET /shelter/all
- PUT /shelter/update/<id>

### Rescue

- POST /rescue/create
- GET /rescue/pending
- PUT /rescue/status/<id>

### Admin

- Dashboard APIs
- User Management APIs

---

## 👩‍💻 Team

Hackathon Project

Developed using Flask, SQLAlchemy, JWT Authentication, and MySQL.

---

## 📄 License

Educational Project
