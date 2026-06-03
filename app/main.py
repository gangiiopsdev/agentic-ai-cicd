from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent injection attacks
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host format')
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}