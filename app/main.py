from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not host or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host input'}
    safe_host = subprocess.escape(host)
    try:
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}