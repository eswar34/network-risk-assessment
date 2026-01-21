# 🔒 Advanced Network Risk Assessment & Security Reporting System

## 📌 Project Overview
This project is a **modern, web-based cybersecurity tool** designed to perform **network reconnaissance, risk assessment, and security report generation**.
It simulates advanced **SOC (Security Operations Center)** activities by scanning target systems, identifying open ports, classifying risk levels, and generating comprehensive security reports.

The application features a **beast-mode UI** with modern design, interactive elements, and professional-grade user experience. Built using **Python, Flask, Nmap**, and cutting-edge web technologies.

---

## 🎯 Key Features
- 🌐 **Modern Web Interface** with glassmorphism design
- 🌓 **Dark/Light Mode Toggle** with localStorage persistence
- 🔍 **Advanced Network Scanning** using Nmap
- 🚪 **Interactive Port Detection** with visual grid display
- ⚠️ **Smart Risk Classification** (Low/Medium/High) with color coding
- 📊 **Data Visualization** using Chart.js for risk assessment
- ⏳ **Loading Animations** with step-by-step progress tracking
- 📱 **Fully Responsive** design for all devices
- 🔐 **Real-time Form Validation** with visual feedback
- 📄 **Professional Security Reports** with download functionality
- 🛡️ **Security Tips Integration** during scanning process
- 📦 **Dockerized** for easy deployment

---

## ✨ UI/UX Enhancements
- **Bootstrap 5** framework with custom styling
- **Font Awesome** icons throughout the interface
- **Smooth animations** and hover effects
- **Interactive loading screens** with progress indicators
- **Professional gradient backgrounds**
- **Glassmorphism effects** with backdrop blur
- **Responsive grid layouts** for port visualization
- **Color-coded risk assessment cards**
- **Modern form controls** with validation

---

## 🛠️ Technologies Used
- **Python 3.14** (Latest version)
- **Flask** (Web Framework)
- **Nmap** (Network Scanner)
- **Bootstrap 5** (CSS Framework)
- **Chart.js** (Data Visualization)
- **Font Awesome** (Icons)
- **HTML5 & CSS3** (Modern Web Standards)
- **JavaScript ES6+** (Interactive Features)
- **Docker** (Containerization)
- **Git & GitHub** (Version Control)

---

## 🏗️ Project Architecture
```
User (Browser)
    ↓
Flask Web Application
    ↓
Interactive Loading Page
    ↓
Nmap Network Scan
    ↓
Risk Analysis Logic
    ↓
Advanced Result Display
    ↓
Security Report Generation
```

---

## 📂 Project Structure
```
network-risk-assessment/
│── app.py                 # Main Flask application
│── scanner.py            # Nmap scanning logic
│── analyzer.py           # Risk analysis algorithms
│── report.py             # Report generation
│── requirements.txt      # Python dependencies
│── Dockerfile           # Docker configuration
│── .gitignore           # Git ignore rules
│── README.md            # Project documentation
│
├── templates/
│   ├── index.html        # Advanced home page with dark mode
│   ├── loading.html      # Interactive loading screen
│   └── result.html       # Professional results dashboard
│
└── static/               # (Future: CSS/JS assets)
```

---

## ⚙️ How It Works
1. **User Input**: Enter IP address or domain with real-time validation
2. **Loading Screen**: Interactive progress with security tips
3. **Network Scan**: Nmap performs comprehensive port scanning
4. **Risk Analysis**: Algorithm classifies security risk levels
5. **Results Display**: Modern dashboard with charts and visualizations
6. **Report Generation**: Professional security report created automatically

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8+ installed
- Nmap installed on system
- Git (for cloning)

### Installation & Setup
```bash
# Clone the repository
git clone https://github.com/eswar34/network-risk-assessment.git
cd network-risk-assessment

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Nmap (if not already installed)
# Windows: Download from https://nmap.org/download.html
# Linux/Mac: Use package manager

# Run the application
python app.py
```

### Access the Application
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 🐳 Docker Deployment
```bash
# Build Docker image
docker build -t network-risk-scanner .

# Run container
docker run -p 5000:5000 network-risk-scanner
```

---

## ✅ Safe Testing Targets
- `scanme.nmap.org` (Official Nmap test host)
- `127.0.0.1` (Localhost for testing)
- `example.com` (Safe public domain)

**⚠️ WARNING**: Do NOT scan unauthorized or production systems without explicit permission.

---

## 📊 Sample Features Showcase

### 🏠 Home Page
- Modern gradient background with glassmorphism
- Interactive form with real-time validation
- Dark/Light mode toggle
- Professional animations and transitions

### ⏳ Loading Screen
- Step-by-step scanning progress
- Security tips during analysis
- Smooth animations and visual feedback

### 📈 Results Dashboard
- Risk level visualization with charts
- Interactive port grid display
- Color-coded security assessment
- Professional report generation

---

## 🎓 Learning Outcomes
- **SOC Workflows**: Understanding security operations
- **Network Security**: Hands-on Nmap usage
- **Python Automation**: Security tool development
- **Modern Web Development**: Flask, Bootstrap, JavaScript
- **UI/UX Design**: Professional interface design
- **Docker Deployment**: Containerization best practices
- **Ethical Hacking**: Responsible security testing

---

## 👨‍💻 Author
**Eswar Kumar**
- Cybersecurity & SOC Analyst Aspirant
- Full-Stack Developer
- GitHub: [eswar34](https://github.com/eswar34)
- LinkedIn: [Your LinkedIn Profile]

---

## 📜 License & Disclaimer
**Educational Purpose Only**

This project is developed for **educational and ethical learning purposes only**. It demonstrates cybersecurity concepts and modern web development practices.

**⚠️ Legal Notice**:
- Unauthorized scanning of systems is illegal
- Always obtain explicit permission before testing
- Use only against systems you own or have permission to test
- Respect privacy and legal boundaries

---

## 🤝 Contributing
Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📞 Support
For questions or issues:
- Open an [issue](https://github.com/eswar34/network-risk-assessment/issues) on GitHub
- Check the [documentation](./docs/) for detailed guides

---

## 🔄 Version History
- **v2.0** - Major UI/UX overhaul with modern design
- **v1.0** - Initial release with basic functionality

---

*Made with ❤️ for the cybersecurity community*
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
GitHub: https://github.com/eswar34

📜 Disclaimer
This project is for educational and ethical learning purposes only.
Unauthorized scanning of systems is illegal and strictly discouraged.
