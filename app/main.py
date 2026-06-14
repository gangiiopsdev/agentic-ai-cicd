from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    # Basic validation: allow only alphanumeric characters and a limited set of symbols
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.'
    for char in host:
        if char not in allowed_chars:
            return False
    return True