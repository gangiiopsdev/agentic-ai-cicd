from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input before using it in subprocess.run
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    # Use shlex.quote to safely escape the command arguments
    import shlex
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], check=True, timeout=5)

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}