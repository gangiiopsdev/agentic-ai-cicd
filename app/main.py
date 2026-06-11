from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Ensure the host is sanitized to avoid injection attacks
    if not host.isalnum() or '..' in host:
        return {'status': 'error', 'output': 'Invalid hostname'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}