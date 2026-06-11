from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError('Invalid host name')
    return host.strip().lower()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}