from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if os.path.exists('/sbin/ping'):
        safe_ping(host)
    else:
        raise Exception('Ping executable not found')
    return {'status': 'completed'}