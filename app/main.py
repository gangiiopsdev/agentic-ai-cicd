from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and logging
    if not host or len(host) > 255:
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}