from fastapi import FastAPI
import subprocess
import ipaddress

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using safe approach
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {"status": "failed", "error": "Invalid IP address"}
    output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    return {"status": "completed", "output": output.decode()}

@app.get("/ping_safe")
def ping_safe(host: str):
    # Secure implementation using safe approach
    try:
        ipaddress.ip_address(host)
    except ValueError:
        return {"status": "failed", "error": "Invalid IP address"}
    output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
    return {"status": "completed", "output": output.decode()}