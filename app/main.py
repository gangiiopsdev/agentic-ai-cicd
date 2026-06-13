from fastapi import FastAPI
import subprocess
import shlex
def sanitize_input(host: str) -> str:
    if not host.isalnum():
        raise ValueError('Invalid host')
    return host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    subprocess.run(shlex.split(f'ping {sanitized_host}'), check=True)
    return {'status': 'completed'}