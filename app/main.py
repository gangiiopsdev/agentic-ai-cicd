from fastapi import FastAPI
import subprocess
def sanitize_host(host: str) -> str:
    allowed_hosts = {'localhost', '127.0.0.1'}
    return host.strip() if host in allowed_hosts else None

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if sanitized_host:
        subprocess.call(['ping', sanitized_host])
    else:
        return {'error': 'Invalid host'}

    return {'status': 'completed'}