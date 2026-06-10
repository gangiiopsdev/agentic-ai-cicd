from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}