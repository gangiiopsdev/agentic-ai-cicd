from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in '-.' for c in v):
            raise ValueError('Invalid host name')
        return v

@app.post('/ping', response_model=str)
def ping(request: PingRequest):
    result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
    return result.stdout