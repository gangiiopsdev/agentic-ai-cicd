from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with input validation
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def is_valid_host(hostname: str) -> bool:
    # Basic validation to ensure the hostname does not contain unexpected characters
    if not hostname.isalnum() and '-' not in hostname and '.' not in hostname:
        return False
    return True