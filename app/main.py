from fastapi import FastAPI
import subprocess
from shlex import quote
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it does not contain malicious commands
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host parameter')
    command = ['ping', quote(host)]
    subprocess.call(command)
    return {'status': 'completed'}