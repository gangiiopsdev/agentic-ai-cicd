from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    # Ensure the host input is sanitized before use
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    secure_ping(host)
    return {'status': 'completed'}