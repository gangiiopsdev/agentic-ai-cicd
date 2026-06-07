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

    # Use a safe method to execute the ping command
    import os
    args = ['ping', host]
    try:
        output = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}