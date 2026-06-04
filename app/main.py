from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Further validate input to ensure it is a valid hostname
    if not host.isalnum() or '.' not in host:
        return {'status': 'error', 'message': 'Invalid hostname'}
    command = ['ping', *shlex.split(host)]
    subprocess.call(command)
    return {'status': 'completed'}