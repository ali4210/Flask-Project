# Flask Web Application with MariaDB

[![Python Version](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-orange.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

> A full-stack web application built with Flask and MariaDB, featuring remote database connectivity, REST API integration, and trainer management system.

![Architecture](https://via.placeholder.com/800x200/4A90E2/FFFFFF?text=Flask+%2B+MariaDB+Architecture)

---

## 📋 Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## ✨ Features

### Core Functionality
- 🎯 **Trainer Management System** - Complete CRUD operations for trainer records
- 🗄️ **Remote Database Access** - MariaDB on Linux, Flask on Windows
- 🌐 **REST API Integration** - Jira API and IP geolocation services
- 📱 **Responsive Templates** - HTML/CSS with Jinja2 templating
- 🔒 **Secure Connections** - Parameterized queries to prevent SQL injection
- 📊 **Data Visualization** - Dynamic table rendering with database records

### Technical Highlights
- **Cross-Platform Architecture**: Windows client connecting to Linux database server
- **Network Communication**: TCP/IP over LAN with MySQL protocol
- **Virtual Environment**: Isolated Python dependencies
- **Error Handling**: Comprehensive exception management
- **Modular Design**: Separation of concerns (routes, templates, database)

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   System Architecture                    │
└─────────────────────────────────────────────────────────┘

Windows PC (Client)              Linux Server (Database)
─────────────────────            ───────────────────────
│                                │
│  Flask Application             │  MariaDB Server
│  ├── Routes                    │  ├── alnafi database
│  ├── Templates                 │  ├── trainer_details table
│  ├── Static Files              │  └── Port 3306
│  └── Port 5000                 │
│                                │
└────────── LAN (192.168.0.x) ───┘
            │
            ├── HTTP Requests
            ├── SQL Queries
            └── API Calls (External)
```

### Technology Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Backend** | Flask 3.1.2, Python 3.13 |
| **Database** | MariaDB 10.x |
| **API Integration** | Requests library, Jira API |
| **Server** | Werkzeug development server |

---

## 🔧 Prerequisites

### Software Requirements

**Windows Development Machine:**
```bash
- Python 3.13+
- pip (Python package manager)
- Git (optional)
- Web browser (Chrome, Firefox, etc.)
```

**Linux Database Server:**
```bash
- MariaDB Server 10.x
- SSH access
- Firewall access to port 3306
```

### Network Requirements
- Both machines on same LAN or accessible via IP
- Port 3306 open on Linux server
- Stable network connection

---

## 📥 Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/flask-mariadb-app.git
cd flask-mariadb-app
```

### Step 2: Create Virtual Environment

**Windows:**
```powershell
python -m venv myproject
.\myproject\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv myproject
source myproject/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed Flask-3.1.2 flask-mysqldb-2.0.0 ...
```

### Step 4: Setup Database

**On Linux Server:**
```bash
# Install MariaDB
sudo apt update
sudo apt install mariadb-server -y

# Secure installation
sudo mysql_secure_installation

# Create database and user
sudo mysql -u root -p
```

**SQL Commands:**
```sql
CREATE DATABASE alnafi;
CREATE USER 'root'@'192.168.0.%' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON alnafi.* TO 'root'@'192.168.0.%';
FLUSH PRIVILEGES;

USE alnafi;
CREATE TABLE trainer_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(100) NOT NULL,
    lname VARCHAR(100) NOT NULL,
    desig VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Configure Remote Access:**
```bash
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
# Change: bind-address = 0.0.0.0

sudo ufw allow 3306/tcp
sudo systemctl restart mariadb
```

---

## ⚙️ Configuration

### Environment Variables

Create `.env` file in project root:

```bash
# Database Configuration
DB_HOST=192.168.0.150
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=alnafi

# Flask Configuration
FLASK_SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# Jira API (Optional)
JIRA_URL=https://your-domain.atlassian.net
JIRA_USER=your-email@company.com
JIRA_API_TOKEN=your-api-token
```

### Application Configuration

Edit `Alnafi_Web/app.py`:

```python
# Update these values
app.config['MYSQL_HOST'] = 'YOUR_LINUX_SERVER_IP'
app.config['MYSQL_USER'] = 'YOUR_DB_USER'
app.config['MYSQL_PASSWORD'] = 'YOUR_DB_PASSWORD'
app.config['MYSQL_DB'] = 'alnafi'
```

---

## 🚀 Usage

### Starting the Application

```bash
# Navigate to application directory
cd Alnafi_Web

# Run Flask application
python app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://0.0.0.0:5000
Press CTRL+C to quit
```

### Accessing the Application

**From Same Computer:**
```
http://localhost:5000/
http://127.0.0.1:5000/
```

**From Other Computers on Network:**
```
http://YOUR_PC_IP:5000/
```

### Available Routes

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Home page |
| `/contacts` | GET | Contact information |
| `/trainer` | GET | Trainer registration form |
| `/trainer_create` | POST | Create new trainer |
| `/trainer_data` | GET | View all trainers |

### Using the Application

**1. Register New Trainer:**
- Open: `http://localhost:5000/trainer`
- Fill form with trainer details
- Click "Submit"
- Data saved to MariaDB database

**2. View All Trainers:**
- Open: `http://localhost:5000/trainer_data`
- See table with all registered trainers
- Data fetched from MariaDB in real-time

**3. Test API Scripts:**
```bash
# Test IP lookup
python API_test.py

# Test Jira integration (configure credentials first)
python API_test_2.py

# Test HTTP headers
python API_test_with_Header.py
```

---

## 📡 API Documentation

### Internal Routes

#### Create Trainer
```http
POST /trainer_create
Content-Type: application/x-www-form-urlencoded

fname=John&lname=Doe&desig=Developer&username=johndoe&password=pass123
```

**Response:**
```
200 OK - Trainer created successfully
```

#### Get All Trainers
```http
GET /trainer_data
```

**Response:**
```html
200 OK - HTML table with trainer records
```

### External API Integration

#### IP Geolocation (ipify.org)
```python
import requests

response = requests.get("https://api.ipify.org?format=json")
data = response.json()
print(data['ip'])  # Your public IP
```

#### Jira Issue Creation
```python
import requests
import json

url = "https://your-domain.atlassian.net/rest/api/3/issue"
headers = {"Content-Type": "application/json"}
payload = {
    "fields": {
        "project": {"key": "PROJECT_KEY"},
        "summary": "Issue Title",
        "description": "Issue Description",
        "issuetype": {"name": "Task"}
    }
}

response = requests.post(url, auth=(email, api_token), 
                        headers=headers, data=json.dumps(payload))
```

---

## 📁 Project Structure

```
Flask/
├── 📄 README.md                    # This file
├── 📄 requirements.txt             # Python dependencies
├── 📄 .gitignore                   # Git ignore rules
├── 📄 .env                         # Environment variables (not in git)
│
├── 📁 Alnafi_Web/                  # Main web application
│   ├── 📄 app.py                   # Flask routes & database logic
│   ├── 📄 config.py                # Configuration settings
│   │
│   ├── 📁 templates/               # HTML templates
│   │   ├── 📄 index.html           # Home page
│   │   ├── 📄 demo.html            # Demo template
│   │   ├── 📄 trainer_details.html # Registration form
│   │   ├── 📄 display_trainer.html # Trainer list view
│   │   └── 📄 style.css            # Styles
│   │
│   └── 📁 static/                  # Static assets
│       ├── 📁 css/                 # Stylesheets
│       ├── 📁 js/                  # JavaScript files
│       └── 📁 images/              # Images
│           ├── 📄 alnafi.jpg
│           └── 📄 abd4.png
│
├── 📁 Flask_Project/               # Simple Flask example
│   └── 📁 myproject/               # Virtual environment
│       └── 📄 app.py               # Basic Flask app
│
├── 📁 myproject/                   # Virtual environment (not in git)
│   ├── 📁 Scripts/                 # Windows executables
│   ├── 📁 Lib/                     # Python packages
│   └── 📄 pyvenv.cfg               # Venv configuration
│
├── 📄 API_test.py                  # IP lookup test
├── 📄 API_test_2.py                # Jira issue creation
├── 📄 API_test_with_Header.py      # HTTP headers demo
├── 📄 API_testing.py               # IP geolocation test
├── 📄 Jira_API_accountID_to_email.py  # Jira user lookup
│
└── 📁 logs/                        # Application logs (not in git)
    └── 📄 flask_app.log            # Error and info logs
```

---

## 🧪 Testing

### Manual Testing

**Test Database Connection:**
```bash
python test_connection.py
```

**Expected output:**
```
✅ Successfully connected to MariaDB!
Tables in database: [('trainer_details',)]
```

### Automated Testing

**Run all tests:**
```bash
python test_application.py
```

**Run specific test:**
```bash
python test_application.py FlaskAppTests.test_home_route
```

**Test coverage:**
```bash
pip install coverage
coverage run test_application.py
coverage report
```

### Test Checklist

- [ ] Database connection successful
- [ ] Home route returns 200 OK
- [ ] Trainer form loads correctly
- [ ] Form submission creates database record
- [ ] Trainer list displays all records
- [ ] API tests run without errors

---

## 🚢 Deployment

### Development Server (Current Setup)

```bash
python app.py
# Runs on http://0.0.0.0:5000
```

### Production Deployment

**Using Gunicorn (Linux):**
```bash
pip install gunicorn
gunicorn --workers=4 --bind=0.0.0.0:5000 app:app
```

**Using systemd (Auto-start):**
```ini
# /etc/systemd/system/flask-app.service
[Unit]
Description=Flask Application
After=network.target

[Service]
User=youruser
WorkingDirectory=/path/to/Flask/Alnafi_Web
Environment="PATH=/path/to/Flask/myproject/bin"
ExecStart=/path/to/Flask/myproject/bin/gunicorn --workers=4 --bind=0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

**Enable service:**
```bash
sudo systemctl enable flask-app
sudo systemctl start flask-app
```

### Nginx Reverse Proxy

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/Flask/Alnafi_Web/static;
    }
}
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

### How to Contribute

1. **Fork the repository**
2. **Create feature branch:** `git checkout -b feature/AmazingFeature`
3. **Commit changes:** `git commit -m 'Add AmazingFeature'`
4. **Push to branch:** `git push origin feature/AmazingFeature`
5. **Open Pull Request**

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions
- Write meaningful commit messages
- Add tests for new features

### Reporting Bugs

Use GitHub Issues with:
- Clear description
- Steps to reproduce
- Expected vs actual behavior
- System information (OS, Python version)

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Saleem Ali

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 👤 Contact

**Saleem Ali**
- **LinkedIn:** [linkedin.com/in/saleem-ali-189719325](https://www.linkedin.com/in/saleem-ali-189719325/)
- **GitHub:** [github.com/ali4210](https://github.com/ali4210)
- **Institution:** Al-Nafi International College (AIOps Program)

**Project Links:**
- **GitHub Repository:** [github.com/ali4210/flask-mariadb-app](https://github.com/ali4210/flask-mariadb-app)
- **Documentation:** [Master Guide](docs/MASTER_GUIDE.md)
- **Issues:** [GitHub Issues](https://github.com/ali4210/flask-mariadb-app/issues)

---

## 🙏 Acknowledgments

- **Flask Documentation** - Excellent framework documentation
- **MariaDB Community** - Database support and resources
- **Stack Overflow** - Problem-solving assistance
- **Al-Nafi International College** - Educational support
- **Open Source Community** - Inspiration and learning

---

## 📊 Project Status

- ✅ **Completed:** Core functionality, database integration, API testing
- 🔄 **In Progress:** User authentication, advanced features
- 📋 **Planned:** Mobile app, advanced analytics, Docker deployment

---

## 🎯 Roadmap

### Version 1.1.0 (Planned)
- [ ] User authentication system
- [ ] Password hashing
- [ ] Session management
- [ ] Input validation

### Version 1.2.0 (Planned)
- [ ] Admin dashboard
- [ ] File upload functionality
- [ ] Email notifications
- [ ] Advanced search

### Version 2.0.0 (Future)
- [ ] RESTful API endpoints
- [ ] JWT authentication
- [ ] Real-time updates (WebSockets)
- [ ] Docker containerization

---

## 💡 Tips & Tricks

### Quick Commands

```bash
# Restart Flask app quickly
Ctrl+C    # Stop server
python app.py    # Restart

# Check database connection
python -c "import mysql.connector; conn = mysql.connector.connect(host='192.168.0.150', user='root', password='8601', database='alnafi'); print('✅ Connected' if conn.is_connected() else '❌ Failed')"

# View logs in real-time
tail -f logs/flask_app.log

# Quick database backup
mysqldump -u root -p alnafi > backup_$(date +%Y%m%d).sql
```

### Common Issues

**Port Already in Use:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [PID_NUMBER] /F

# Linux
sudo lsof -t -i:5000 | xargs kill -9
```

**Database Connection Failed:**
```bash
# Check if MariaDB is running
sudo systemctl status mariadb

# Test connection
telnet 192.168.0.150 3306
```

---

**Last Updated:** December 23, 2024  
**Version:** 1.0.0  
**Status:** Active Development

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with ❤️ by [Saleem Ali](https://github.com/ali4210)

</div>
