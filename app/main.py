from fastapi import FastAPI
import subprocess
from typing import Optional

generate_ping_command = lambda host: f'ping {host}' if isinstance(host, str) and len(host.split()) == 1 else None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: Optional[str] = None):
    if host:
        command = generate_ping_command(host)
        if command:
            try:
                subprocess.run(command, check=True, shell=False, capture_output=True, text=True)
                return {'status': 'completed'}
            except subprocess.CalledProcessError as e:
                return {'status': 'failed', 'error': str(e)}
    return {'status': 'invalid_host'}