from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid characters in host parameter')
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {'status': 'completed'}