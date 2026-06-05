from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and input validation
    if not host or not host.strip() or not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "error", "output": "Invalid input"}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}