from fastapi import FastAPI
import subprocess
import re
from pydantic import BaseModel

app = FastAPI()

# Define a whitelist of allowed hosts for security reasons
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping_endpoint(request: PingRequest):
    if request.host not in ALLOWED_HOSTS:
        raise ValueError('Host is not allowed')
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}