from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    # Validate the host to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'output': 'Invalid hostname'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'output': 'Invalid hostname'}
    return safe_ping(host)