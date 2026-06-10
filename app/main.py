from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize user input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    # Secure implementation using subprocess.run with a list of arguments to prevent shell injection
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {"status": "completed"}