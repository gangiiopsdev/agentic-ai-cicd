from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host:
        return {'error': 'Host parameter is required'}, 400
    if len(host) > 255 or ' ' in host or '\' in host or ';' in host or '|' in host or '&' in host:
        return {'error': 'Invalid host parameter'}, 400
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}