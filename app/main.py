from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host to prevent shell injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}