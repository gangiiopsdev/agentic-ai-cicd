from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Unauthorized host')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    subprocess.run(['ping', sanitized_host], check=True)
    return {'status': 'completed'}