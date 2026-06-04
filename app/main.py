from fastapi import FastAPI
import subprocess

global ping

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum() or '.' in host:
        return {'error': 'Invalid host'}, 400
    subprocess.call(['ping', '-c', '1', host])