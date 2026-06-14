from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}

    subprocess.call(['ping', host])

    return {'status': 'completed'}