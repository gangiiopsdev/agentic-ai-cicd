from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    valid_hosts = ['example.com', 'test.com']
    if host in valid_hosts:
        return host
    else:
        raise ValueError('Invalid host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}