from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and input validation
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True, timeout=5)
    return {'status': 'completed'}