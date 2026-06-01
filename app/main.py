from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    result = subprocess.run(['ping', '-c', str(1), request.host], capture_output=True, text=True)
    return {
        'host': request.host,
        'result': result.stdout
    }