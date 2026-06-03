from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host):
    # Validate and sanitize the host input more rigorously
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {"status": "completed", "response": result.stdout}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    response = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "response": response.stdout}