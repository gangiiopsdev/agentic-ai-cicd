from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with proper validation and sanitization
    if not host.strip():
        raise ValueError('Host parameter cannot be empty or whitespace only.')
    subprocess.call(['ping', host])
    return {'status': 'completed'}