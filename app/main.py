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

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    # Sanitize the input before using it in subprocess
    sanitized_host = subprocess.list2cmdline([request.host])
    subprocess.run(['ping', '-c 1', sanitized_host], check=True, shell=False)
    return {'status': 'completed'}