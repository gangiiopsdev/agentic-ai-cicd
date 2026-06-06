from fastapi import FastAPI
import subprocess
g import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}