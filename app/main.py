from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation
    if not host or len(host) > 255:
        raise ValueError('Invalid host input')
    subprocess.call(['ping', host])