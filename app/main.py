from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host])
    return {'status': 'completed'}

# Example of a simple host validation function
def validate_host(hostname: str) -> bool:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    return all(c in allowed_chars for c in hostname)