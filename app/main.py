from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host input')
    subprocess.call(['ping', host])
    return {'status': 'completed'}