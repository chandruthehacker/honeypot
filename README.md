# 🛡️ Honeypot Trap Logger

**Track & Analyze Intrusion Attempts with a Low-Interaction Honeypot**

![Honeypot Banner](https://chandruthehacker.github.io/portfolio-website-old/projects/all-projects/honeypot/assets/images/honeypot.webp)

## 🔍 Project Overview

A simple yet effective Python-based honeypot that simulates an admin login portal. It captures access attempts, logs attacker behavior (IP, credentials, user-agent, etc.), and helps in identifying suspicious patterns. Ideal for educational or demo environments.

## 🧰 Tools & Technologies

- **Languages:** Python, HTML, CSS
- **Framework:** Flask
- **Tech Stack:** Logging, Honeypot, JSONL, Regex (optional)
- **Environment:** Tested on Kali Linux, WSL2

## ✨ Key Features

- 🎭 Fake login interface mimicking a real admin panel
- 🛑 Logs both page visits and credential submission
- 🌐 Tracks IP address, user-agent, username, password, and request path
- 📁 Separate logs for access and login attempts
- ⚙️ Extendable for threat detection, alerts, or anomaly analysis

## 📂 File Structure

<pre>
honeypot/
├── honeypot.py
├── requirements.txt
├── templates/
│ ├── admin_login.html
│ └── access_denied.html
├── static/
│ └── style.css
├── logs/
│ ├── access_logs.jsonl
│ └── login_attempts.jsonl
└── README.md
</pre>


## 🚀 Getting Started

### 🔧 Step 1: Clone the Repository

```bash
git clone https://github.com/chandruthehacker/honeypot.git
cd honeypot
```

### 🧪 Step 2: Create and Activate Virtual Environment

- On Linux / macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

- On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 📦 Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### ▶️ Step 4: Run the Honeypot

```bash
python honeypot.py
```

## 📊 Sample Log Output

```json
{
  "timestamp": "2025-06-10T10:33:00.458694",
  "ip": "172.23.192.1",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
  "method": "POST",
  "path": "/admin",
  "username": "admin",
  "password": "123456"
}
```

## 🌐 Project Details
- [Blog](https://chandruthehacker.github.io/portfolio/projects/all-projects/honeypot/honeypot.html)
- [View All Projects](https://chandruthehacker.github.io/portfolio/projects/projects.html)

---

## 🧠 Final Thoughts

This project demonstrates how a simple honeypot can be used to study attacker behavior in a controlled, low-interaction environment. It's a great learning tool for aspiring cybersecurity professionals to understand logging, threat detection, and data analysis fundamentals.

Feel free to customize and expand this project by adding alert systems, dashboards, or integrating with SIEM tools like Splunk or ELK Stack.

---

## 👨‍💻 Author

**Chandraprakash C**  
🎓 BSc Computer Science | 🔐 Cybersecurity Enthusiast  
📧 [cyberchandru87@gmail.com](mailto:cyberchandru87@gmail.com)  
🌐 [GitHub](https://github.com/chandruthehacker) • [LinkedIn](https://linkedin.com/in/chandraprakash87/)

---

> ⚠️ **Disclaimer**: This project is intended for **educational purposes only**. Do not deploy or run honeypots in live environments without proper authorization and precautions.




