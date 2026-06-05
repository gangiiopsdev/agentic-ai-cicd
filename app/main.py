from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}