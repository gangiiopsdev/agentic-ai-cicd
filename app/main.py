from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

@app.post("/ping")
def ping(request: PingRequest):
    subprocess.call(f"ping {request.host}", shell=False)
    return {"status": "completed"}