from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid hostname'}
    subprocess.run(shlex.split(f'ping {host}'))
    return {'status': 'completed'}