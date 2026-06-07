from fastapi import FastAPI
import subprocess
import shlex
global host
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isnumeric() or len(host) > 3:
        return {'status': 'error', 'message': 'Invalid host'}
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)
    return {'status': 'completed'}