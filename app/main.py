from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, value):
        allowed_hosts = ['google.com', 'example.com']  # Replace with actual allowed hosts
        if value not in allowed_hosts:
            raise ValueError(f'Invalid host: {value}')
        return value

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    command = ['ping', request.host]
    # Use check_output instead of run for better error handling and output capture
    try:
        result = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': result.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}