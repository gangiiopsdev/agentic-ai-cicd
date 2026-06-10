from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str
    @validator('host')
    def check_host(cls, v):
        if not v.startswith(('127.0.0.1', '::1')) and not v.isdigit():
            raise ValueError('Invalid host address')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    subprocess.call(['ping', request.host])
    return {'status': 'completed'}