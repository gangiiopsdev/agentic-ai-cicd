from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def check_host(cls, v):
        allowed_hosts = ['127.0.0.1', '::1']
        if v not in allowed_hosts and not v.isdigit():
            raise ValueError('Invalid host address')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True, shell=False)
    return {'status': 'completed'}