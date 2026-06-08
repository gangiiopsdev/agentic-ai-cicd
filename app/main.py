from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Use subprocess.run with split arguments to prevent shell injection
    subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host name')
    safe_ping(host)
    return {"status": "completed"}