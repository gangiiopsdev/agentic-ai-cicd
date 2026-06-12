from fastapi import FastAPI
import subprocess
def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    # Safe implementation
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Basic regex to allow alphanumeric and special characters typically found in hostnames/IP addresses
        return "Invalid host"
    return safe_ping(host)