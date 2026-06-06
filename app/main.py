from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}