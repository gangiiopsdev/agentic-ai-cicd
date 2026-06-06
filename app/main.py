from fastapi import FastAPI
import subprocess
import re
def safe_ping(host):
    # Validate the input to ensure it's a safe hostname/IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid input')
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)