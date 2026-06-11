from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
import os
class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v
app = FastAPI()
@app.get("/ping")
def ping(request: PingRequest):    try:
        # Sanitize the host input to avoid shell injection
        sanitized_host = os.path.basename(request.host)
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise Exception('Ping command failed')
        return {'status': 'completed'}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}