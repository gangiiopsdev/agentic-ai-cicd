from fastapi import FastAPI
import subprocess
import re
def safe_ping(host):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return result.stdout

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    response = safe_ping(host)
    return {"status": "completed", "output": response}