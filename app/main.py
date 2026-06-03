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
def safe_execute(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.post('/ping')
def ping(request: PingRequest):
    command = ['ping', request.host]
    return safe_execute(command)