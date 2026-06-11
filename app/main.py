from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError("Invalid host name")

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid host name")
    subprocess.call(['ping', host], shell=False)
    return {"status": "completed"}