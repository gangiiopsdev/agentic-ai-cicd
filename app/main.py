from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', 'localhost']  # Define a list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}. Allowed hosts are {allowed_hosts}')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True)
    return {"status": "completed"}