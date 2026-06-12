from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
class PingRequest(BaseModel):
    host: str
    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.example.com']  # List of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v
app = FastAPI()
@app.get("/ping")
def ping(request: PingRequest):
    subprocess.call(['ping', request.host], shell=False)  # Ensure shell=False to avoid shell injection