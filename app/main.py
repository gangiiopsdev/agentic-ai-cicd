from fastapi import FastAPI
import subprocess
def sanitize_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host if host in allowed_hosts else None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host is not None:
        subprocess.run(['ping', sanitized_host], check=True)
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}