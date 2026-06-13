from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and sanitization
    allowed_hosts = ['127.0.0.1', '::1']  # Allow only local hosts for demonstration purposes
    if host in allowed_hosts:
        command = shlex.split(f'ping {host}')
        subprocess.run(command, check=True)
    else:
        raise ValueError('Invalid host')
    return {'status': 'completed'}