I have designed a professional, high-impact `README.md` for your GitHub repository.

This file is crafted to immediately tell a recruiter or technical lead that you understand **Systems Architecture**, not just coding. It highlights the "Hybrid" nature of your project (Windows + Linux), which is a major selling point.

---

### 📄 README.md

*Create a file named `README.md` in the root of your repository and paste this content:*

```markdown
# Hybrid Cloud & Automation Portfolio: Flask, Linux, & APIs

**Author:** Saleem Ali
**Architecture:** Hybrid Client-Server (Windows Client -> Remote Linux Database)
**Domain:** Full Stack Development & DevOps Automation

---

## ==>> Project Overview

This repository demonstrates a production-grade **Hybrid Architecture** where the Application Layer is decoupled from the Data Layer. Unlike a standard "localhost" project, this system mimics a real-world enterprise environment.

* **The Application (Windows):** A Python Flask web server that handles the User Interface, business logic, and external API integrations (Jira).
* **The Database (Linux):** A virtualized MariaDB server running on a Linux instance, configured to accept secure remote connections over TCP/IP.

This portfolio proves the ability to bridge the gap between **Software Engineering** (Python/Web) and **IT Infrastructure** (Linux/Networking).

---

## ==>> System Architecture

[Insert Architecture Diagram Here]

**Data Flow:**
1.  **User** interacts with the Web Dashboard on the Windows Client.
2.  **Flask** processes the request (e.g., "Register New Trainer").
3.  **Application** opens a socket connection to the Linux VM (`192.168.0.150`) on Port 3306.
4.  **MariaDB** executes the SQL Transaction and returns the result.
5.  **Jinja2** renders the live data back to the user.

---

## ==>> Tech Stack & Tools

| Category | Technologies Used |
| :--- | :--- |
| **Backend** | Python 3.x, Flask, Jinja2 |
| **Database** | MariaDB (MySQL), SQL |
| **Operating Systems** | Windows 10/11 (Client), Linux (Server/DB) |
| **Automation** | REST APIs, Jira Integration, Request Library |
| **Networking** | TCP/IP, Firewall Config (UFW), Bind Address Management |
| **Frontend** | HTML5, CSS3, Dynamic Templating |

---

## ==>> Key Features

### 1. Trainer Management Portal
A full CRUD (Create, Read, Update, Delete) interface for managing Trainer profiles.
* **Dynamic Tables:** Uses Jinja2 loops to render SQL rows instantly.
* **Data Integrity:** Direct integration with the backend Linux database.

### 2. Automated Jira Ticketing
Includes a standalone Python automation suite for Atlassian Jira.
* **Function:** Automatically generates "Task" or "Bug" tickets via the Jira REST API.
* **Security:** Uses API Token authentication (Basic Auth) rather than raw passwords.

### 3. Hybrid Networking Configuration
Demonstrates advanced system administration skills:
* Configured **MariaDB Bind Address** to listen on `0.0.0.0` (Public Network).
* Managed **Linux UFW (Uncomplicated Firewall)** to allow traffic on Port 3306.
* Established a stable bridge between the Host OS and Guest VM.

---

## ==>> Installation & Setup

This project requires two machines (or a Host PC and a Virtual Machine).

### Part 1: Linux Database Server (The Backend)
*Run these commands on your Linux VM.*

1.  **Install MariaDB:**
    ```bash
    sudo apt update && sudo apt install mariadb-server
    ```
2.  **Allow Remote Connections:**
    * Edit `/etc/mysql/mariadb.conf.d/50-server.cnf`.
    * Set `bind-address = 0.0.0.0`.
3.  **Configure Firewall:**
    ```bash
    sudo ufw allow 3306/tcp
    ```
4.  **Create Database & User:**
    ```sql
    CREATE DATABASE alnafi;
    GRANT ALL PRIVILEGES ON alnafi.* TO 'root'@'%' IDENTIFIED BY 'YOUR_PASSWORD';
    FLUSH PRIVILEGES;
    ```

### Part 2: Windows Application (The Client)
*Run these commands on your local machine.*

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourUsername/flask-hybrid-automation.git](https://github.com/YourUsername/flask-hybrid-automation.git)
    cd flask-hybrid-automation
    ```
2.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Connection:**
    * Open `Alnafi_Web/app.py`.
    * Update `app.config['MYSQL_HOST']` to your Linux IP address.
4.  **Run the Application:**
    ```bash
    python Alnafi_Web/app.py
    ```
    * Access the dashboard at `http://localhost:5000`.

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

## ==>> Contact

**Saleem Ali**

* **Role:** Full Stack Engineer & Automation Specialist
* **Focus:** Bridging the gap between Development and Infrastructure.

```

***



### 💡 My Recommendation
I have inserted a placeholder `[Insert Architecture Diagram Here]` in the README code above.

Since this is a "Hybrid Architecture" project, a simple diagram showing a **Windows Laptop** connected to a **Linux Server** icon via a line labeled "Port 3306" would look incredibly professional.

**Would you like me to generate that specific Architecture Diagram for you right now so you can upload it to your repo?**

```