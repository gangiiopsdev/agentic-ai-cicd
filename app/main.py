from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
import os

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Sanitize the host input to avoid shell injection
        sanitized_host = os.path.basename(request.host)
        subprocess.run(['ping', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}