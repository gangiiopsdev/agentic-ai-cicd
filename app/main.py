from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    allowed_hosts = ['google.com', 'example.com']  # List of allowed hosts
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}