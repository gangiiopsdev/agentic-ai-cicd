from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('.'):
            raise ValueError('Invalid host format')
        return v

@app.get("/ping")
def ping_endpoint(request: PingRequest):
    subprocess.call(['ping', '-c 1', request.host], shell=False)