from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not is_safe_host(host):
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])
    return {'status': 'completed'}

def is_safe_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
    return host in allowed_hosts