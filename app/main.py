from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate or sanitize host input to prevent command injection
    if not host.isalnum() and host.count('.') != 3:
        raise ValueError('Invalid host address')
    subprocess.call(['ping', host])
    return {'status': 'completed'}