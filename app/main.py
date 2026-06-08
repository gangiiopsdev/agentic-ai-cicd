from fastapi import FastAPI
import re
def safe_ping(host):
    # Using subprocess.run instead of subprocess.call for better security
    # Sanitize the host parameter by validating it against a whitelist or using a regular expression
    allowed_hosts = ['example.com', '127.0.0.1']
    if not re.match(r'^([a-zA-Z0-9.-]+)$', host):
        raise ValueError("Invalid host")
    if host not in allowed_hosts:
        raise ValueError("Invalid host")
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get="/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}