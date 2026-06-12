from fastapi import FastAPI
import subprocess
from shlex import quote
import os

def safe_ping(host: str):
    try:
        result = subprocess.run(["ping", "-c", "1", quote(host)], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input to ensure it is a valid IP address or hostname
    if not re.match(r'^([0-9]{1,3}\.){3}[0-9]{1,3}$', host) and not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return "Invalid host"
    return safe_ping(host)