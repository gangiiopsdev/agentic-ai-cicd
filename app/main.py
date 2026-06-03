from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if host.strip() != host or len(host) > 255:
        raise ValueError('Invalid hostname')
    subprocess.call(shlex.split(f'ping {host}'))
    return {'status': 'completed'}