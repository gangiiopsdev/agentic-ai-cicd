from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Sanitize the host parameter using shlex.quote
    sanitized_host = subprocess.list2cmdline([host])
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        raise ValueError("Invalid host")
    subprocess.run(['ping', '-c', '1', sanitized_host], shell=False, check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}