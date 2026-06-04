from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str) -> dict:
    # Secure implementation
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host input')
    subprocess.call(['ping', '-c 1', host])
    return {'status': 'completed'}