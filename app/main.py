from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1']  # Replace with appropriate validation logic
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(f'ping {request.host}', shell=False)
    return {'status': 'completed'}