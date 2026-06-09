from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or '.' not in host:
        return {'status': 'invalid_host'}
    subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed'}