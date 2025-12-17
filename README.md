
# Hybrid Cloud & Automation Portfolio: Flask, Linux, & APIs

**Author:** Saleem Ali
**Architecture:** Hybrid Client-Server (Windows Client -> Remote Linux Database)
**Domain:** Full Stack Development, DevOps, & Systems Architecture

---

## ==>> Project Overview

This repository demonstrates a production-grade **Hybrid Architecture** where the Application Layer is decoupled from the Data Layer. Unlike standard single-machine projects, this system mimics a real-world enterprise environment involving cross-platform communication.

* **The Application (Windows):** A Python Flask web server that handles the User Interface, business logic, and external API integrations (Jira).
* **The Database (Linux):** A virtualized MariaDB server running on a Linux instance, configured to accept secure remote connections over TCP/IP.

This portfolio proves the ability to bridge the gap between **Software Engineering** (Python/Web) and **IT Infrastructure** (Linux/Networking).

---

## ==>> System Architecture

The system relies on a TCP/IP bridge between the local host (Windows) and the virtualized server (Linux).

```mermaid
graph LR
    subgraph Host_A_Windows [Windows PC (Client)]
        Flask[Python Flask App]
        Browser[Web Dashboard]
        Scripts[Automation Scripts]
        Browser --> Flask
    end

    subgraph Host_B_Linux [Linux VM (Server)]
        DB[(MariaDB Database)]
        Firewall[UFW Firewall]
    end

    subgraph External_Cloud [External APIs]
        Jira[Jira Cloud]
        IPServices[IPify API]
    end

    %% Connections
    Flask -- "SQL Query (Port 3306)" --> Firewall
    Firewall --> DB
    Scripts -- "REST API (HTTPS)" --> Jira
    Scripts -- "GET Request" --> IPServices

    %% Styling
    style Host_A_Windows fill:#f9f9f9,stroke:#333,stroke-width:2px
    style Host_B_Linux fill:#e1f5fe,stroke:#333,stroke-width:2px
    style Flask fill:#2980b9,color:white
    style DB fill:#c0392b,color:white

```

**Data Flow:**

1. **User** interacts with the Web Dashboard on the Windows Client.
2. **Flask** processes the request (e.g., "Register New Trainer").
3. **Application** opens a socket connection to the Linux VM (Target IP) on Port 3306.
4. **MariaDB** executes the SQL Transaction and returns the result over the network.
5. **Jinja2** renders the live data back to the user.

---

## ==>> Tech Stack

| Category | Technologies Used |
| --- | --- |
| **Backend** | Python 3.x, Flask, Jinja2 |
| **Database** | MariaDB (MySQL), SQL |
| **Infrastructure** | Windows 10/11 (Client), Linux (Server), Virtualization |
| **Networking** | TCP/IP, Port Forwarding, Firewall Config (UFW) |
| **Automation** | REST APIs, Jira Integration, Request Library |

---

## ==>> Installation & Configuration

Since this is a hybrid project, setup is divided into two parts.

### => Part 1: Linux Server Configuration (The Backend)

*Perform these steps on your Linux Virtual Machine.*

1. **Install MariaDB:**
```bash
sudo apt update && sudo apt install mariadb-server
sudo systemctl enable mariadb

```


2. **Configure Remote Access (Bind Address):**
* By default, MariaDB blocks remote connections.
* Edit config: `sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf`
* Change: `bind-address = 127.0.0.1` to `bind-address = 0.0.0.0`
* Restart: `sudo systemctl restart mariadb`


3. **Configure Firewall:**
* Allow traffic on the database port.


```bash
sudo ufw allow 3306/tcp
sudo ufw reload

```


4. **Create Database & Grant Remote Privileges:**
* Log in to SQL: `sudo mysql -u root -p`


```sql
CREATE DATABASE alnafi;
USE alnafi;

-- Create Table
CREATE TABLE trainer_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fname VARCHAR(100),
    lname VARCHAR(100),
    desig VARCHAR(100),
    username VARCHAR(50),
    password VARCHAR(50)
);

-- Grant access to root from ANY IP (%)
GRANT ALL PRIVILEGES ON alnafi.* TO 'root'@'%' IDENTIFIED BY '8601';
FLUSH PRIVILEGES;
EXIT;

```



### => Part 2: Windows Client Configuration (The App)

*Perform these steps on your local Windows machine.*

1. **Clone the Repository:**
```bash
git clone [https://github.com/YourUsername/flask-hybrid-automation.git](https://github.com/YourUsername/flask-hybrid-automation.git)
cd flask-hybrid-automation

```


2. **Install Python Dependencies:**
```bash
pip install -r requirements.txt

```


3. **Configure Network Connection:**
* Find your Linux VM's IP address (Run `ip addr` on Linux).
* Open `Alnafi_Web/app.py`.
* Update the configuration:


```python
app.config['MYSQL_HOST'] = '192.168.0.150' # Replace with your Linux IP
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '8601'

```


4. **Run the Application:**
```bash
python Alnafi_Web/app.py

```


* Access the dashboard at `http://localhost:5000`.



---

## ==>> Key Features

### 1. Trainer Management Portal

A full CRUD (Create, Read, Update, Delete) interface for managing Trainer profiles.

* **Architecture:** MVC Pattern (Model-View-Controller).
* **Frontend:** Dynamic HTML tables generated via Jinja2 loops.
* **Backend:** Secure SQL transactions over a network socket.

### 2. Automated Jira Ticketing

Includes a standalone Python automation suite for Atlassian Jira.

* **Function:** Automatically generates "Task" or "Bug" tickets via the Jira REST API.
* **Security:** Uses API Token authentication (Basic Auth).
* **Usage:** Update `API_test_2.py` with your Jira credentials and run.

### 3. Network Diagnostics

Includes `API_test.py` to verify external connectivity and fetch Public IP / Geo-location data programmatically.

---

## ==>> Project Structure

```text
├── Alnafi_Web/
│   ├── app.py                 # Main Flask Application Entry Point
│   └── templates/             # HTML/Jinja2 User Interface
│       ├── index.html         # Main Dashboard
│       ├── trainer_details.html # Data Entry Form
│       └── display_trainer.html # Data View
├── Scripts/
│   ├── API_test_2.py          # Jira Automation Script
│   └── API_test.py            # IP & Connectivity Checker
├── requirements.txt           # Project Dependencies
└── README.md                  # Documentation

```

---

## ==>> Troubleshooting

**Issue: "Can't connect to MySQL server on '192.168.x.x' (10060)"**

* **Solution 1:** Ensure your VM Network Adapter is set to **"Bridged Adapter"** so it has a reachable IP.
* **Solution 2:** Verify you edited the `bind-address` in the Linux MariaDB config to `0.0.0.0`.
* **Solution 3:** Check if the Linux Firewall is blocking port 3306 (`sudo ufw status`).

**Issue: "Access denied for user 'root'@'192.168.x.x'"**

* **Solution:** You missed the SQL Grant step. Run `GRANT ALL ... TO 'root'@'%'` on the Linux DB.

---

## ==>> Contact

**Saleem Ali**

* **Role:** Full Stack Engineer & Automation Specialist
* **Focus:** Bridging the gap between Development and Infrastructure.

```

```
