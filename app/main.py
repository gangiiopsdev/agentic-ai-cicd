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
    if not host.isdigit() or len(host) != 3:
        raise ValueError('Invalid host format')
    subprocess.run(['ping', os.path.abspath(host)], check=True)
    return {'status': 'completed'}