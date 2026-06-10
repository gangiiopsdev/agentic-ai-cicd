from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    if not host.isalnum():
        raise ValueError("Invalid host name")

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {'status': 'completed'}