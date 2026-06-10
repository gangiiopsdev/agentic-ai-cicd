from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Preventing command injection by limiting hosts
    if not host.startswith('localhost'):
        return {'error': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}