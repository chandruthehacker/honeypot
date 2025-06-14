from flask import Flask, request, render_template, redirect
import os, json, datetime

app = Flask(__name__)

# Configuration
LOG_DIR = "logs"
ACCESS_LOG_FILE = os.path.join(LOG_DIR, "access_logs.jsonl")
LOGIN_LOG_FILE = os.path.join(LOG_DIR, "login_attempts.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)

# Logging functions
def log_access(data):
    data["timestamp"] = datetime.datetime.now().isoformat()
    with open(ACCESS_LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")

def log_login_attempt(data):
    data["timestamp"] = datetime.datetime.now().isoformat()
    with open(LOGIN_LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")

# Routes
@app.route("/", methods=["GET"])
def home():
    return redirect("/admin")

@app.route("/admin", methods=["GET", "POST"])
def fake_login():
    data = {
        "ip": request.remote_addr,
        "method": request.method,
        "path": request.path,
        "user_agent": request.headers.get("User-Agent", "N/A"),
    }
    if request.method == "POST":
        data.update({
            "username": request.form.get("username", ""),
            "password": request.form.get("password", "")
        })
        log_login_attempt(data)
        return redirect("/access_denied")
    log_access(data)
    return render_template("admin.html")

@app.route("/access_denied", methods=["GET"])
def access_denied():
    data = {
        "ip": request.remote_addr,
        "method": request.method,
        "path": request.path,
        "user_agent": request.headers.get("User-Agent", "N/A"),
    }
    log_access(data)
    return render_template("access_denied.html")

if __name__ == '__main__':
    print(f"Honeypot running on http://0.0.0.0:8000")
    app.run(host='0.0.0.0', port=8000)
