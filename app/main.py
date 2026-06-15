from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to prevent injection attacks
    if not host or len(host) > 255:
        return {"status": "failed", "error": "Invalid host name"}

    # Allow only certain patterns for hostnames
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not pattern.match(host):
        return {"status": "failed", "error": "Invalid hostname format"}

    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}