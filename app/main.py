from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent shell injection
    if not host.isalnum() or '.' in host:
        raise ValueError('Invalid host name')
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}