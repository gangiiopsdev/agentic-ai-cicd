from fastapi import FastAPI
import subprocess
import re
def ping(host: str):
    # Secure implementation using subprocess.run with full path and input validation
    try:
        result = subprocess.run(['/usr/bin/ping', host], check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)
global app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid input")
    return ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}