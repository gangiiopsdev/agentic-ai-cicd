from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if not host.startswith('localhost'):  # Preventing command injection by limiting hosts
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}