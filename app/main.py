from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Ensure host is sanitized before passing to subprocess
    if not host.strip():
        raise ValueError('Invalid host input')
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}