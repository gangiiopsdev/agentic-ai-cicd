from fastapi import FastAPI
import subprocess
from pydantic import validator

def validate_host(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    return host

class PingRequest(BaseModel):
    host: str = validator(validate_host)

app = FastAPI()

@app.get('/ping')
def ping(request: PingRequest):
    try:
        subprocess.check_output(['ping', '-c', '1', request.host], stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}