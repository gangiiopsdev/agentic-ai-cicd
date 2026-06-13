from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', '::1']  # Define a list of allowed hosts
        if v in allowed_hosts:
            return v
        raise ValueError('Invalid host')

@app.post("/ping")
def ping(request: PingRequest):
    subprocess.call(['ping', '--', request.host])  # Use '--' to prevent command injection
    return {'status': 'completed'}