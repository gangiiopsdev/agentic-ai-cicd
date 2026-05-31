from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Additional validation to ensure the host parameter is safe
    if not all(c.isalnum() or c in '.-' for c in host):
        raise ValueError('Invalid input detected in host parameter')
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}