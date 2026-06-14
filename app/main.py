from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, timeout=5)
    return {'status': 'completed'}