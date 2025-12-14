# Web-Based Network Risk Assessment & Security Reporting System

## 📌 Project Overview
This project is a web-based cybersecurity tool designed to perform **network reconnaissance, risk assessment, and security report generation**.  
It simulates basic **SOC (Security Operations Center)** activities by scanning a target system, identifying open ports, classifying risk levels, and generating a security report.

The application is built using **Python, Flask, and Nmap**, and deployed using **Docker** for real-world usability.

---

## 🎯 Key Features
- 🌐 Web-based interface for easy interaction  
- 🔍 Network scanning using **Nmap**
- 🚪 Detection of open TCP ports
- ⚠️ Risk classification (Low / Medium / High)
- 📄 Automatic security report generation
- 🧑‍💻 SOC-oriented design and workflow
- 📦 Dockerized for deployment

---

## 🛠️ Technologies Used
- **Python 3**
- **Flask** (Web Framework)
- **Nmap** (Network Scanner)
- **HTML & Embedded CSS**
- **Docker**
- **Git & GitHub**

---

## 🏗️ Project Architecture
User (Browser)
↓
Flask Web Application
↓
Nmap Network Scan
↓
Risk Analysis Logic
↓
Result Display + Report Generation

yaml
Copy code

---

## 📂 Project Structure
soc_web_project/
│── app.py
│── scanner.py
│── analyzer.py
│── report.py
│── Dockerfile
│── requirements.txt
│── README.md
│
└── templates/
├── index.html
└── result.html

yaml
Copy code

---

## ⚙️ How It Works
1. User enters an IP address or domain name
2. The backend runs an Nmap scan
3. Open ports are extracted from scan results
4. Risk level is calculated based on exposed services
5. Results are displayed on the web page
6. A detailed security report is generated automatically

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3 installed
- Nmap installed
- Flask installed

### Steps
```bash
pip install flask
python app.py
Open browser:

cpp
Copy code
http://127.0.0.1:5000
🐳 Docker Deployment
Build Docker Image
bash
Copy code
docker build -t network-risk-scanner .
Run Container
bash
Copy code
docker run -p 5000:5000 network-risk-scanner
✅ Safe Testing Targets
scanme.nmap.org (Official Nmap test host)

127.0.0.1 (Localhost)

⚠️ Do NOT scan unauthorized or production systems.

📄 Sample Report Contents
Target details

Scan timestamp

Open ports

Risk level

Security recommendations

🎓 Learning Outcomes
Understanding SOC workflows

Hands-on experience with Nmap

Python automation for security tasks

Web application development with Flask

Docker-based deployment

Secure and ethical testing practices

👨‍🎓 Author
Eswar Kumar
Cybersecurity & SOC Analyst Aspirant
GitHub: https://github.com/YOUR_USERNAME

📜 Disclaimer
This project is for educational and ethical learning purposes only.
Unauthorized scanning of systems is illegal and strictly discouraged.