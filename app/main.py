from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, value):
        allowed_hosts = ['example.com', 'localhost']  # Define a list of allowed hosts
        if value not in allowed_hosts:
            raise ValueError(f'Host {value} is not allowed. Only {allowed_hosts} are permitted.')
        return value

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(["ping", request.host])  # Use shell=False to avoid command injection
    return {"status": "completed"}