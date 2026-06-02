from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True, capture_output=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}