from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the input
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.call(['ping', host])
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}