I have updated your Master Guide to perfectly reflect your **Hybrid Architecture** (Windows Application + Linux Database). I have merged the previous code snippets with the specific networking configurations needed to make them talk to each other.

As per your strict guidelines, I have removed all emojis and used the `==>>` and `=>` formatting style.

Here is your **Ultimate Universal Master Guide**.

---

# Flask Hybrid Architecture Portfolio: Windows App & Linux Database

**Author:** Saleem Ali
**Architecture:** Client-Server (Windows Flask App connecting to Linux MariaDB)
**Tech Stack:** Python 3.x, Flask, MariaDB, Jinja2, REST APIs

## ==>> Project Overview

This project demonstrates a production-grade architecture where the Application Layer is decoupled from the Data Layer.

* **Host A (Windows PC):** Runs the Python Flask Web Server and API Automation Scripts.
* **Host B (Linux VM):** Hosts the MariaDB Database Engine.
* **Connectivity:** The Flask app communicates via TCP/IP over Port 3306 to perform real-time CRUD operations on the Linux server.

---

## ==>> Comprehensive Index

| Module | Topic | Description |
| --- | --- | --- |
| **1. Linux Server Setup** | `MariaDB Config` | Configuring Linux to accept remote connections (Bind Address). |
| **2. Windows Env Setup** | `pip` & `venv` | Setting up the local development environment. |
| **3. Database Schema** | `SQL Script` | Creating the database and granting remote user privileges. |
| **4. Web Backend** | `app.py` | The complete Flask logic with remote connection strings. |
| **5. Frontend UI** | `templates/` | HTML Forms and Jinja2 Displays. |
| **6. API Tools** | `API_test.py` | Jira & IP Automation scripts. |

---

## ==>> Module 1: Linux Database Server Configuration

*Action: Perform these steps inside your Linux Terminal (Host B).*

### => Step 1: Install & Enable MariaDB

```bash
sudo apt update
sudo apt install mariadb-server
sudo systemctl start mariadb
sudo systemctl enable mariadb

```

### => Step 2: Configure Remote Access (Crucial)

By default, MariaDB only listens to itself (Localhost). You must open it to the network.

1. Edit the configuration file:
```bash
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

```


2. Locate the line: `bind-address = 127.0.0.1`
3. Change it to:
```ini
bind-address = 0.0.0.0

```


4. Save (`Ctrl+O`, `Enter`) and Exit (`Ctrl+X`).
5. Restart the service to apply changes:
```bash
sudo systemctl restart mariadb

```



### => Step 3: Configure Linux Firewall

Allow traffic on the database port (3306).

```bash
sudo ufw allow 3306/tcp
sudo ufw reload

```

*Note: Run `ip addr show` to confirm your Linux IP (e.g., `192.168.0.150`).*

---

## ==>> Module 2: Database Schema & Privileges

*Action: Run these SQL commands inside the Linux MariaDB shell.*

### => Step 1: Create Database & Table

```sql
-- Login to SQL
-- sudo mysql -u root -p

CREATE DATABASE alnafi;
USE alnafi;

CREATE TABLE trainer_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(100),
    lname VARCHAR(100),
    desig VARCHAR(100),
    username VARCHAR(50),
    password VARCHAR(50)
);

```

### => Step 2: Grant Remote Permissions (The Bridge)

You must explicitly allow the user to connect from a remote IP (Your Windows machine). using `%` allows connections from ANY IP.

```sql
-- Syntax: GRANT ALL ON database.* TO 'user'@'source_ip' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON alnafi.* TO 'root'@'%' IDENTIFIED BY '8601';

FLUSH PRIVILEGES;
EXIT;

```

---

## ==>> Module 3: Windows Application Environment

*Action: Perform these steps on your Windows PC (Host A).*

### => Step 1: Dependencies (`requirements.txt`)

Create this file and install using `pip install -r requirements.txt`.

```text
Flask
flask-mysqldb
requests
mysql-connector-python

```

### => Step 2: The Flask Application (`app.py`)

This is the complete, corrected code. Note the `MYSQL_HOST` configuration pointing to your Linux VM.

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# => Universal Remote DB Config
# Replace '192.168.0.150' with your actual Linux VM IP if it changes
app.config['MYSQL_HOST'] = '192.168.0.150' 
app.config['MYSQL_USER'] = 'root'          # Matches the user created in Module 2
app.config['MYSQL_PASSWORD'] = '8601'      # Matches the password created in Module 2
app.config['MYSQL_DB'] = 'alnafi'
mysql = MySQL(app)

# => Dashboard Routes
@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('sample.html', title="Contact Us")

@app.route("/tsheet")
def tsheet():
    return render_template('demo.html', title="Time Sheet")

@app.route("/reports")
def searchform():
    return render_template('sample.html', title="Reports")

# => Trainer Management (CRUD)
@app.route("/trainer")
def trainer():
    return render_template('trainer_details.html')

@app.route("/trainer_create", methods=['GET', 'POST'])
def trainer_create():
    if request.method == "POST":
        # 1. Fetch Data form HTML Form
        fname = request.form['fname']
        lname = request.form['lname']
        desig = request.form['desig']
        username = request.form['username']
        password = request.form['password']
        
        # 2. Insert into Remote Linux DB
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO trainer_details (fname, lname, desig, username, password) VALUES (%s, %s, %s, %s, %s)"
        val = (fname, lname, desig, username, password)
        cursor.execute(sql, val)
        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('trainer_data'))
    return render_template('trainer_details.html')

@app.route("/trainer_data")
def trainer_data():
    # 1. Fetch all records from Remote DB
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM trainer_details")
    rows = cursor.fetchall()
    cursor.close()
    
    # 2. Pass to Template
    return render_template('display_trainer.html', trainers=rows)

if __name__ == "__main__":
    # Host 0.0.0.0 makes the Windows App accessible on the local network too
    app.run(debug=True, host="0.0.0.0", port=5000)

```

---

## ==>> Module 4: Frontend User Interface

*Key templates required in the `templates/` folder.*

### => Input Form (`trainer_details.html`)

Connects the UI to the `/trainer_create` route.

```html
<html>
<body>
    <h1>Register Trainer</h1>
    <form method="post" action="{{ url_for('trainer_create') }}">
        First Name: <input type="text" name="fname"><br>
        Last Name: <input type="text" name="lname"><br>
        Designation: <input type="text" name="desig"><br>
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>

```

### => Output View (`display_trainer.html`)

Dynamically renders rows fetched from the Linux database.

```html
<html>
<body>
    <table border="1">
        <tr>
            <th>ID</th><th>First Name</th><th>Last Name</th>
            <th>Designation</th><th>Username</th>
        </tr>
        {% for trainer in trainers %}
        <tr>
            <td>{{ trainer[0] }}</td>
            <td>{{ trainer[1] }}</td>
            <td>{{ trainer[2] }}</td>
            <td>{{ trainer[3] }}</td>
            <td>{{ trainer[4] }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>

```

---

## ==>> Module 5: API Automation Scripts

*Standalone tools to run on Windows.*

### => Jira Automation (`API_test_2.py`)

```python
import requests, json

# Configuration
JIRA_URL = "https://your-domain.atlassian.net"
ENDPOINT = f"{JIRA_URL}/rest/api/3/issue"
USER = "your_email@example.com"
TOKEN = "your_api_token"

headers = {"Accept": "application/json", "Content-Type": "application/json"}

payload = json.dumps({
    "fields": {
        "project": {"key": "IIP"},
        "summary": "Automated Issue via Python",
        "description": "Created from Windows Client",
        "issuetype": {"name": "Task"},
        "priority": {"name": "High"}
    }
})

try:
    response = requests.post(ENDPOINT, auth=(USER, TOKEN), headers=headers, data=payload)
    response.raise_for_status()
    print(f"Success! Issue Key: {response.json().get('key')}")
except Exception as e:
    print(f"Failed: {e}")

```

---

## ==>> Troubleshooting Hybrid Connectivity

If your Windows App cannot talk to the Linux DB, check these common failure points:

1. **Ping Test:**
* Open Windows CMD: `ping 192.168.0.150`
* If this fails, your VM Network Adapter is likely set to "NAT". Change it to **"Bridged Adapter"** in your VM settings so it gets a real IP address on your network.


2. **Bind Address:**
* If `netstat -ant | grep 3306` on Linux shows `127.0.0.1:3306`, you missed Step 2 in Module 1. It must say `0.0.0.0:3306`.


3. **User Access:**
* If you get "Access denied for user 'root'@'192.168.x.x'", you missed the `GRANT ALL... TO 'root'@'%'` step in Module 2.