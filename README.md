# 🚨 ResQAI – AI-Powered Disaster Response & Rescue Management System

> An intelligent disaster response and rescue management platform that enables victims to request emergency assistance, rescue teams to coordinate operations, and administrators to monitor disaster relief activities in real time.

---

## 📖 Overview

**ResQAI** is a Flask-based backend application developed during a hackathon to streamline disaster response operations. The platform provides secure authentication, role-based access control, SOS request management, shelter monitoring, and rescue team coordination through RESTful APIs.

The system is designed to improve emergency response efficiency by allowing:

- 🆘 Victims to instantly send SOS requests
- 🚑 Rescue teams to manage rescue operations
- 🏠 Administrators to monitor shelters and disaster activities
- 🔐 Secure access using JWT Authentication

---

## ✨ Key Features

### 🔐 Authentication & Authorization

- User Registration
- Secure Login
- JWT Authentication
- Role-Based Access Control (RBAC)

Supported Roles:

- 👤 Victim
- 🚑 Rescue Team
- 👨‍💼 Administrator

---

## 🆘 SOS Management

Victims can quickly raise emergency requests during disasters.

Features include:

- Create SOS Requests
- View SOS Details
- Update SOS Status
- Delete SOS Requests
- Track Request Progress

---

## 🚑 Rescue Management

Designed for rescue personnel to efficiently coordinate emergency operations.

Features include:

- Create Rescue Teams
- View Pending SOS Requests
- Assign Rescue Teams
- Update Rescue Status
- Monitor Active Rescue Missions

---

## 🏠 Shelter Management

Administrators can efficiently manage relief shelters.

Features include:

- Add Shelters
- View Available Shelters
- Update Shelter Information
- Delete Shelters
- Manage Shelter Capacity

---

## 👨‍💼 Admin Dashboard

Provides complete control over the disaster management system.

Features include:

- User Management
- Shelter Management
- Rescue Monitoring
- Dashboard Analytics
- System Administration APIs

---

# 🛠️ Tech Stack

## Backend

- Python
- Flask
- Flask-JWT-Extended
- SQLAlchemy

## Database

- MySQL

## API Testing

- Thunder Client

## Version Control

- Git
- GitHub

---

# 📁 Project Structure

```
ResQAI/
│
├── app.py                  # Application Entry Point
├── config.py               # Configuration Settings
├── extensions.py           # Database & JWT Initialization
├── requirements.txt        # Project Dependencies
│
├── models/                 # Database Models
├── routes/                 # API Routes
├── utils/                  # Helper Functions
│
└── README.md
```

---

# 🔑 Authentication

ResQAI uses **JWT (JSON Web Tokens)** for secure authentication.

After successful login, include the generated token in every protected API request.

Example:

```http
Authorization: Bearer <YOUR_JWT_TOKEN>
```

---

# 📡 REST API Endpoints

## 🔐 Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login user |

---

## 🆘 SOS APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/sos/create` | Create SOS request |
| GET | `/sos/all` | View all SOS requests |
| GET | `/sos/<id>` | View specific SOS |
| PUT | `/sos/update/<id>` | Update SOS |
| DELETE | `/sos/delete/<id>` | Delete SOS |

---

## 🏠 Shelter APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/shelter/create` | Add shelter |
| GET | `/shelter/all` | View shelters |
| PUT | `/shelter/update/<id>` | Update shelter |
| DELETE | `/shelter/delete/<id>` | Delete shelter |

---

## 🚑 Rescue APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/rescue/create` | Create rescue team |
| GET | `/rescue/pending` | View pending SOS requests |
| PUT | `/rescue/status/<id>` | Update rescue status |
| PUT | `/rescue/assign/<id>` | Assign rescue team |

---

## 👨‍💼 Admin APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/admin/dashboard` | Dashboard Overview |
| GET | `/admin/users` | Manage Users |
| GET | `/admin/shelters` | Monitor Shelters |
| GET | `/admin/rescue` | Monitor Rescue Operations |

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/ResQAI.git
```

```bash
cd ResQAI
```

---

### Create Virtual Environment

Windows

```bash
python -m venv venv
```

Mac/Linux

```bash
python3 -m venv venv
```

---

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure MySQL

Create a MySQL database.

Update the database credentials in:

```
config.py
```

---

### Run the Application

```bash
python app.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

# 🧪 API Testing

The APIs can be tested using:

- Thunder Client (VS Code)
- Postman
- Insomnia

---

# 🔒 Security

- JWT Authentication
- Password Hashing
- Role-Based Authorization
- Protected API Endpoints
- SQLAlchemy ORM
- Secure Database Access

---

# 🚀 Future Enhancements

- 🤖 AI-Based Disaster Severity Prediction
- 🗺️ Live GPS Tracking
- 📍 Real-Time Rescue Team Locations
- 📡 Satellite & Weather API Integration
- 📲 Mobile Application
- 🔔 Push Notifications
- 📊 Interactive Admin Dashboard
- 🧠 AI Resource Allocation
- 🗺️ Interactive Disaster Heatmaps

---

# 👥 Team

**ResQAI** was developed as a **Hackathon Project** by a passionate team focused on leveraging Artificial Intelligence to improve disaster response and emergency management.

---

# 📜 License

This project is developed for **educational and hackathon purposes**.

Feel free to use it for learning and academic projects.

---

# ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.

It motivates us to continue building impactful open-source projects.

---

> **"Saving lives through intelligent technology."** 🚨🤖
