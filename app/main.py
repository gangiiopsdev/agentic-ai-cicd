from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('127.0.0.1'):  # Allow only localhost for simplicity
            raise ValueError('Only localhost is allowed')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    subprocess.call(args)
    return {'status': 'completed'}