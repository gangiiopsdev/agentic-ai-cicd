from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'status': 'error', 'message': 'Invalid host name'}
    # Secure implementation
    subprocess.run([os.path.realpath('ping'), host], check=True, capture_output=True)
    return {'status': 'completed'}