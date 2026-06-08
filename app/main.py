from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_wrapper(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

import re
def is_valid_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None