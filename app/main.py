from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}. Only the following hosts are allowed: {allowed_hosts}')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True, shell=False)
    return {'status': 'completed'}