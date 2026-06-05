from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent shell injection
    if not host.isalnum() or not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):#
        return {'error': 'Invalid host'}, 400
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}