from fastapi import FastAPI
import subprocess
import shlex
import re
global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {'status': 'completed'}