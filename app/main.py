from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with check_output and validation
    if not host.isalnum():
        return "Invalid host"
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout
global app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation with validation
    return safe_ping(host)