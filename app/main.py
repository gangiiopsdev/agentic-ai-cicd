from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input further
    if not host.isalnum() or len(host) > 100:
        raise ValueError('Invalid host name')
    # Use a whitelist of allowed hosts
    allowed_hosts = ['8.8.8.8', '8.8.4.4']  # Example allowed IPs
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}