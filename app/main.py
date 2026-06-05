from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent shell injection
    if not host.isdigit() or len(host) > 3:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}