from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to ensure it's safe
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['/usr/bin/ping', host], check=True)
    return {'status': 'completed'}