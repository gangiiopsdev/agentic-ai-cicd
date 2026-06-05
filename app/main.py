from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        return {'status': 'error', 'message': 'Invalid host name'}
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}