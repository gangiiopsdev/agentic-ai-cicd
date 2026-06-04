from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}