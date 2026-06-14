from fastapi import FastAPI
import subprocess
from typing import Optional
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

@app.get('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    safe_ping(request.host)
    return {'status': 'completed'}

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', '-c', '1', host], check=True)