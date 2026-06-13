from fastapi import FastAPI
import subprocess
def execute_ping(host):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise HTTPException(status_code=400, detail="Invalid host")
    response = execute_ping(host)
    return {"status": "completed", "output": response}

import re
def is_valid_host(host):
    # Basic regex to validate a hostname
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None