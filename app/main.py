from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'another-example.com']  # Define a list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(["ping", request.host])
    return {"status": "completed"}