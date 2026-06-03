from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using subprocess.run with validation
    if host.strip() and all(c.isalnum() or c in '.-_' for c in host):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host provided')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}