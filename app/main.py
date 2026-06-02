from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'localhost']  # Define a whitelist of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    safe_host = subprocess.quote(request.host)
    subprocess.call(['ping', safe_host])
    return {'status': 'completed'}