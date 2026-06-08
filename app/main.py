from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

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
    # Validate and sanitize the host input before using it in subprocess
    sanitized_host = subprocess.list2cmdline([request.host])
    try:
        subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500