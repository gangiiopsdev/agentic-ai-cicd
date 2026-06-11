from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with additional sanitization
    if not host.strip().isalnum() or len(host) > 64:
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}