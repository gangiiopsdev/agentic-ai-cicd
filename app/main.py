from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host parameter is required')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    sanitized_host = subprocess.list2cmdline([request.host])
    subprocess.call(['ping', sanitized_host], shell=False)

    return {"status": "completed"}