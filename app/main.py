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
    # Safe implementation with input validation and sanitization
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}