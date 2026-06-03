from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
    if re.match(r'^[a-zA-Z0-9.-]+$', host) and host in allowed_hosts:
        subprocess.call(shlex.split(f'ping {host}'))
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}