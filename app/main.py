from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'output': 'Invalid input'}
    # Safe implementation using subprocess.run without shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}