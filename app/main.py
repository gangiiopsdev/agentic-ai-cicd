from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

# Preventive controls
@app.get("/secure-ping")
def secure_ping(host: str):
    # Validate host to ensure it is a trusted IP or domain
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid host provided."}
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}

# Helper function to validate host
def validate_host(host: str) -> bool:
    # Implement validation logic here (e.g., using regex, IP address checking)
    return True