from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    
    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum():
            raise ValueError('Host must be alphanumeric')
        return v

@app.post('/ping', response_model=str)
def ping_endpoint(request: PingRequest):
    args = ['ping', request.host]
    # Sanitize input to avoid shell injection
    sanitized_host = subprocess.list2cmdline([request.host])
    result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}