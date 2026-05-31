from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', 'localhost']  # Example whitelist
        if v not in allowed_hosts:
            raise ValueError('Host is not allowed')
        return v

app = FastAPI()

@app.post('/ping')
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True, shell=False)
    return {'status': 'completed'}