# 🚀 Flask Web Application - Quick Reference Card

**Version:** 1.0.0 | **Last Updated:** December 2024 | **Printable Format**

---

## ⚡ Quick Start Commands

```bash
# Activate Virtual Environment
.\myproject\Scripts\activate        # Windows
source myproject/bin/activate       # Linux/Mac

# Run Flask Application
cd Alnafi_Web
python app.py

# Access Application
http://localhost:5000/

# Deactivate Environment
deactivate
```

---

## 🗄️ Database Quick Commands

### MariaDB Management
```bash
# Start/Stop/Status
sudo systemctl start mariadb
sudo systemctl stop mariadb
sudo systemctl status mariadb

# Login to Database
sudo mysql -u root -p

# Remote Connection Test
mysql -h 192.168.0.150 -u root -p alnafi
```

### Essential SQL Queries
```sql
-- View All Trainers
SELECT * FROM trainer_details;

-- Search by Name
SELECT * FROM trainer_details WHERE fname LIKE '%John%';

-- Count Total Records
SELECT COUNT(*) FROM trainer_details;

-- Insert New Trainer
INSERT INTO trainer_details (fname, lname, desig, username, password)
VALUES ('John', 'Doe', 'Developer', 'johndoe', 'pass123');

-- Update Record
UPDATE trainer_details SET desig='Senior Dev' WHERE id=1;

-- Delete Record
DELETE FROM trainer_details WHERE id=5;

-- Get Recent Records
SELECT * FROM trainer_details ORDER BY created_date DESC LIMIT 10;
```

---

## 🌐 Flask Routes Reference

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page |
| `/contacts` | GET | Contact information |
| `/trainer` | GET | Registration form |
| `/trainer_create` | POST | Create trainer |
| `/trainer_data` | GET | View all trainers |

---

## 📦 Essential Python Packages

```bash
# Core Dependencies
pip install flask==3.1.2
pip install flask-mysqldb
pip install requests
pip install mysql-connector-python

# Development Tools
pip install python-dotenv
pip install flask-login
pip install wtforms

# Install All from File
pip install -r requirements.txt

# Save Current Packages
pip freeze > requirements.txt
```

---

## 🔧 Flask App Template

```python
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# Database Configuration
app.config['MYSQL_HOST'] = '192.168.0.150'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'alnafi'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def get_data():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM trainer_details")
    data = cursor.fetchall()
    cursor.close()
    return render_template('display.html', records=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

---

## 🔌 Database Connection Pattern

```python
# Standard Pattern
try:
    cursor = mysql.connection.cursor()
    sql = "SELECT * FROM table WHERE column=%s"
    cursor.execute(sql, (value,))
    results = cursor.fetchall()
    mysql.connection.commit()  # For INSERT/UPDATE/DELETE
    cursor.close()
except Exception as e:
    print(f"Error: {e}")
```

---

## 🎯 Common Issues & Solutions

### Issue 1: Can't Connect to Database
```bash
# Check MariaDB Status
sudo systemctl status mariadb

# Test Connection
telnet 192.168.0.150 3306

# Check Firewall
sudo ufw status
sudo ufw allow 3306/tcp
```

### Issue 2: Port Already in Use
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [PID_NUMBER] /F

# Linux
sudo lsof -t -i:5000 | xargs kill -9
```

### Issue 3: Module Not Found
```bash
# Verify Virtual Environment Active
which python  # Should show venv path

# Reinstall Package
pip install flask-mysqldb --force-reinstall
```

### Issue 4: Template Not Found
```bash
# Verify Structure
app.py
templates/
  └── your_template.html

# Check Template Name in Code
return render_template('your_template.html')  # Must match exactly
```

---

## 🔒 Security Checklist

```python
# ✅ DO THIS
# 1. Use Environment Variables
import os
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# 2. Parameterized Queries
cursor.execute("SELECT * FROM users WHERE id=%s", (user_id,))

# 3. Hash Passwords
from werkzeug.security import generate_password_hash
hashed = generate_password_hash('password123')

# 4. Validate Input
from wtforms import Form, StringField, validators
class MyForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])

# ❌ DON'T DO THIS
# 1. Hardcode Passwords
app.config['MYSQL_PASSWORD'] = 'password123'  # NO!

# 2. String Formatting SQL
sql = f"SELECT * FROM users WHERE id={user_id}"  # SQL Injection!

# 3. Plain Text Passwords
password = request.form['password']  # Store hashed only!

# 4. Debug Mode in Production
app.run(debug=True)  # Only in development!
```

---

## 🌍 API Request Templates

### GET Request
```python
import requests

response = requests.get('https://api.example.com/data')
data = response.json()
status = response.status_code
```

### POST Request with Auth
```python
import requests
import json

url = "https://api.example.com/create"
headers = {"Content-Type": "application/json"}
payload = {"key": "value"}
auth = ("username", "password")

response = requests.post(url, 
                        auth=auth,
                        headers=headers, 
                        data=json.dumps(payload))
```

### Error Handling
```python
try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

---

## 📊 HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Success |
| 201 | Created | Resource created |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Login required |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource missing |
| 500 | Server Error | Server crashed |

---

## 🎨 Jinja2 Template Syntax

```html
<!-- Variables -->
{{ variable_name }}
{{ user.name }}

<!-- Conditionals -->
{% if condition %}
    <p>True</p>
{% else %}
    <p>False</p>
{% endif %}

<!-- Loops -->
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}

<!-- Include Template -->
{% include 'header.html' %}

<!-- Extend Template -->
{% extends 'base.html' %}
{% block content %}
    <!-- Your content -->
{% endblock %}
```

---

## 🔗 Database Connection String Format

```python
# MySQL/MariaDB Format
mysql://username:password@host:port/database

# Example
mysql://root:8601@192.168.0.150:3306/alnafi

# SQLAlchemy Format (Alternative)
SQLALCHEMY_DATABASE_URI = 'mysql://root:8601@192.168.0.150/alnafi'
```

---

## 📁 Project Structure Template

```
Flask-Project/
├── app.py                  # Main application
├── config.py               # Configuration
├── requirements.txt        # Dependencies
├── .env                    # Environment variables
├── .gitignore              # Git ignore rules
├── README.md               # Documentation
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   └── form.html
├── static/                 # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── tests/                  # Test files
│   └── test_app.py
└── logs/                   # Log files
    └── app.log
```

---

## 🧪 Testing Commands

```bash
# Run Tests
python test_application.py

# With Coverage
coverage run test_application.py
coverage report
coverage html

# Pytest (if installed)
pytest
pytest -v
pytest tests/test_app.py
```

---

## 🚀 Deployment Quick Guide

### Development Server
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

### Production Server (Gunicorn)
```bash
# Install
pip install gunicorn

# Run
gunicorn --workers=4 --bind=0.0.0.0:5000 app:app

# With Log File
gunicorn --workers=4 --bind=0.0.0.0:5000 --access-logfile access.log app:app
```

---

## 🔍 Debugging Tips

```python
# Print Debugging
print(f"Debug: {variable}")
print(f"Type: {type(variable)}")
print(f"Length: {len(variable)}")

# Flask Debug Mode
app.run(debug=True)  # Shows detailed errors

# Python Debugger
import pdb; pdb.set_trace()
# Commands: n (next), c (continue), p variable (print)

# Logging
import logging
logging.basicConfig(level=logging.DEBUG)
app.logger.debug('Debug message')
app.logger.info('Info message')
app.logger.error('Error message')
```

---

## 💾 Backup Commands

```bash
# Database Backup
mysqldump -u root -p alnafi > backup_$(date +%Y%m%d).sql

# Restore Database
mysql -u root -p alnafi < backup_20241223.sql

# Project Backup (exclude venv)
tar -czf flask_backup_$(date +%Y%m%d).tar.gz \
    --exclude='myproject' \
    --exclude='__pycache__' \
    --exclude='*.pyc' .
```

---

## 🌐 Networking Commands

```bash
# Check IP Address
ipconfig                    # Windows
ifconfig                    # Linux/Mac
ip addr show                # Linux (modern)

# Test Connectivity
ping 192.168.0.150
telnet 192.168.0.150 3306

# Check Open Ports
netstat -ano | findstr :5000        # Windows
sudo lsof -i :5000                  # Linux/Mac
sudo netstat -tulpn | grep :5000    # Linux

# Check Firewall
sudo ufw status                     # Linux
netsh advfirewall show allprofiles  # Windows
```

---

## 📝 Git Quick Commands

```bash
# Initialize Repository
git init

# Stage Files
git add .
git add filename.py

# Commit
git commit -m "Your message"

# Push to Remote
git push origin main

# Pull Changes
git pull origin main

# Check Status
git status

# View History
git log --oneline
```

---

## 🔑 Environment Variables Template

```bash
# .env file
DB_HOST=192.168.0.150
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=alnafi
SECRET_KEY=your-secret-key
FLASK_ENV=development
FLASK_DEBUG=True
```

```python
# Load in Python
from dotenv import load_dotenv
import os

load_dotenv()

app.config['MYSQL_HOST'] = os.getenv('DB_HOST')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
```

---

## 📞 Emergency Contacts & Resources

**Documentation:**
- Flask: https://flask.palletsprojects.com/
- MariaDB: https://mariadb.com/kb/
- Python: https://docs.python.org/3/

**Community Help:**
- Stack Overflow: https://stackoverflow.com/questions/tagged/flask
- Flask Discord: https://discord.gg/pallets
- Reddit: r/flask, r/learnpython

**Project Repository:**
- GitHub: https://github.com/ali4210
- LinkedIn: https://www.linkedin.com/in/saleem-ali-189719325/

---

## 🎯 Performance Quick Tips

```python
# 1. Connection Pooling
app.config['MYSQL_POOL_SIZE'] = 5

# 2. Query Optimization
# Use LIMIT for large datasets
cursor.execute("SELECT * FROM table LIMIT 100")

# 3. Caching (if flask-caching installed)
from flask_caching import Cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.cached(timeout=60)
def expensive_function():
    # Your code here
    pass

# 4. Pagination
page = request.args.get('page', 1, type=int)
per_page = 20
offset = (page - 1) * per_page
```

---

## 📋 Pre-Flight Checklist

**Before Running:**
- [ ] Virtual environment activated
- [ ] Database server running
- [ ] Correct IP address in config
- [ ] All packages installed
- [ ] Templates in correct folder
- [ ] Port 5000 available

**Before Deployment:**
- [ ] Debug mode OFF
- [ ] Passwords in environment variables
- [ ] .gitignore properly configured
- [ ] Database backed up
- [ ] Tests passing
- [ ] Documentation updated

---

## 🏆 Best Practices Summary

✅ **Always use parameterized queries**
✅ **Never commit .env files**
✅ **Hash passwords before storing**
✅ **Use virtual environments**
✅ **Write comprehensive documentation**
✅ **Handle errors gracefully**
✅ **Test before deploying**
✅ **Keep dependencies updated**

---

**🖨️ Print This Card & Keep It Handy!**

**Last Updated:** December 23, 2024  
**Version:** 1.0.0  
**Project:** Flask Web Application with MariaDB

---

**Made with ❤️ for developers everywhere**

*"The best code is well-documented code."*
