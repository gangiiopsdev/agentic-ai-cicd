from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or '..' in host:
        return {'status': 'error', 'error': 'Invalid input'}
    try:
        output = subprocess.check_output(['ping', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}