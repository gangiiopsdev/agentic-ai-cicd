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
    # Secure implementation with input validation
    if not host.isalnum() or not host.strip():
        raise ValueError('Invalid host provided')
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}