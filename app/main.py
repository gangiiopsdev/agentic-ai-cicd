from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    args = shlex.split(f'ping {request.host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}