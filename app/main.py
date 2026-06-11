from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

# Validate host function remains the same
def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in ['-', '.', '_'] for c in host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.call(['ping', '-c 1'] + shlex.split(host))
    return {'status': 'completed'}