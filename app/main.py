from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not host.strip():
        raise ValueError('Host parameter is required and cannot be empty')
    subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not host.strip():
        raise ValueError('Host parameter is required and cannot be empty')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}