from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with proper sanitization
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, text=True)
    return {'status': 'completed'}