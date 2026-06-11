from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate or sanitize the input host
    if not validate_host(host):
        raise ValueError('Invalid host provided')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    return host in allowed_hosts