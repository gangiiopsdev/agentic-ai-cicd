from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.replace('.', '').isnumeric() and len(host.split('.')) == 4:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host format'}
    return {'status': 'completed'}