from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

def validate_host(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return host

@app.get('/ping')
def ping(host: str = validator(validate_host)):  # Validate input with Pydantic validator
    try:
        subprocess.check_output(['ping', '-c', '1', f'"{host}"'], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}