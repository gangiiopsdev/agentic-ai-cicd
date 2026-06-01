from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

app = FastAPI()

@app.post('/ping')
def ping(request: PingRequest):
    result = subprocess.run(['ping', request.host], capture_output=True, text=True, shell=False)
    return result.stdout