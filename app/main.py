from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it's a safe hostname/IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": 'failed', 'error': 'Invalid host'}
    return safe_ping(host)