from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and logging
    if not host.isalnum() or len(host) > 50:
        return {'status': 'error', 'message': 'Invalid hostname'}
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {'status': 'completed'}