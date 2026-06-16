from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Input validation for 'host'
    if not host.isalnum():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}