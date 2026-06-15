from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent command injection
    if not host.isalnum() or len(host) > 20:
        return {'status': 'error', 'message': 'Invalid host parameter'}
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}