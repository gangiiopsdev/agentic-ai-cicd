from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['localhost', '127.0.0.1']
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.get("/ping")
def ping_handler(request: PingRequest):
    subprocess.run(['ping', request.host], check=True)