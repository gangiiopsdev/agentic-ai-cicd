from fastapi import FastAPI
import subprocess

app = FastAPI()

def execute_ping(host: str):
    # Fixed implementation using subprocess.run and list arguments
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        return execute_ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400

import re
def validate_host(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')