from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.call(args)
    return {'status': 'completed'}