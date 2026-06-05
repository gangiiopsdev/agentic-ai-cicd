from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.strip():
        raise ValueError("Invalid hostname")
    allowed_hosts = ['google.com', 'example.com']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        raise ValueError("Hostname not allowed")

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)