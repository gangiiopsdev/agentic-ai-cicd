from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent shell injection
    if not all(c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-' for c in host):#
        return {'error': 'Invalid host'}, 400
    # Use a whitelist of allowed hosts instead of validating against specific characters
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        return {'error': 'Host not allowed'}, 403
    # Safe implementation using subprocess.run with shell=False and capture_output=True
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}