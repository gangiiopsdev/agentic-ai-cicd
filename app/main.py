from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def execute_ping(host: str) -> dict:
    request_body = PingRequest(host=host)
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

class PingRequest(BaseModel):
    host: str

def validate_host(host: str) -> str:
    if any(char in host for char in ';|&<>`$!'):  # Common shell injection characters
        raise ValueError('Invalid host input')
    return host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validated_host = validate_host(host)
    return execute_ping(validated_host)