from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['localhost', '127.0.0.1']
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.call(args, shell=False)
    return {'status': 'completed'}