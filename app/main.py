from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    command_parts = shlex.split(f'ping {host}')
    result = subprocess.run(command_parts, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return safe_ping(host)