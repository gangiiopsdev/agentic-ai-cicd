from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate against a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}