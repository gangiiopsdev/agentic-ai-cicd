from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = shlex.split(f'ping {host}')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

# Fixed code:
@app.get('/ping_fixed')
def ping_fixed(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return {'error': 'Invalid characters in hostname'}
    args = shlex.split(f'ping {host}')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}