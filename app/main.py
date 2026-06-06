from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host or len(host) > 255:
        raise ValueError('Invalid host')
    args = ['ping', host]
    subprocess.run(args, check=True, capture_output=True)
    return {'status': 'completed'}