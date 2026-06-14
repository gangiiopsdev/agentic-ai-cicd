from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.run with full path and validation
    if host == 'localhost' or host.startswith('127.0.0.'):  # Add your own validation logic here
        subprocess.run(['/sbin/ping', host], check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')