from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input before passing it to subprocess
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(['ping', host], shell=False)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate host input before passing it to subprocess
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host"}
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Simple validation for demonstration purposes
    return all(c.isalnum() or c in (('.', '-', '_')) for c in host)