from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.post('/ping')
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.call(args)
    return {'status': 'completed', 'result': result}