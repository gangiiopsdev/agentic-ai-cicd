from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    safe_host = shlex.quote(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True, capture_output=True, text=True)

    return {'status': 'completed'}