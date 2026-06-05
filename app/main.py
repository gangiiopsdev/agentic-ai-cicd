from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator


global ping

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or '.' in v:
            raise ValueError('Invalid host')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    subprocess.call(['ping', '-c', '1', request.host])