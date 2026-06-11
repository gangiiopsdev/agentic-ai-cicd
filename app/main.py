from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        raise ValueError('Invalid host provided')
    subprocess.call(['ping', host])
    return {'status': 'completed'}

# Helper function to validate the host
import re
def is_valid_host(host: str) -> bool:
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None