from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host parameter to ensure it does not contain malicious input
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        return {'error': 'Invalid host parameter'}
    try:
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e}'}