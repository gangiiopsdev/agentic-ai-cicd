from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], capture_output=True, text=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        safe_ping(host)
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe
    return True