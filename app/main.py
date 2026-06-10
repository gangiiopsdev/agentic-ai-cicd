from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname provided')
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {'status': 'completed'}