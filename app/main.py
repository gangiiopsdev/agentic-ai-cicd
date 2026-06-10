from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host.strip() or 'ping' in host.lower():
        raise ValueError("Invalid host")
    
    # Secure implementation
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)