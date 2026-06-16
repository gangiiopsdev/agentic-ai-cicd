from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(host: str):
    command = ['ping', host]
    try:
        output = subprocess.check_output(command, universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Secure fix: Validate input before using it in the command
@app.post('/ping_secure')
def ping_secure(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    command = ['ping', host]
    try:
        output = subprocess.check_output(command, universal_newlines=True, timeout=5)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}