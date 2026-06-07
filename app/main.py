from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not host.strip().replace('.', '').isdigit():
        raise ValueError('Invalid host format')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}