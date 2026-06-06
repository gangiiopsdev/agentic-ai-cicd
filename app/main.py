from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():  # Basic validation to prevent injection
        raise ValueError('Invalid input for host')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}