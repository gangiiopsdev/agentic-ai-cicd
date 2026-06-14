from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}