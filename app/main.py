from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True, timeout=5)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    # Secure implementation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True, timeout=5)
    return {'status': 'completed'}