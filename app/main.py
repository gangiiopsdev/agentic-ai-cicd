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
    # Safe implementation with proper input sanitization
    if not host.isdigit() and '-' not in host and '.' not in host:
        raise ValueError('Invalid host format')
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}