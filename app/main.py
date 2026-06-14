from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
from fastapi.middleware.security import SecurityMiddleware

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.strip():
            raise ValueError('Host cannot be empty')
        return v

app = FastAPI()

@app.get("/ping")
def ping(request: PingRequest):
    # Validate and sanitize the host input before using it in subprocess
    sanitized_host = request.host.replace('.', '_').replace('-', '_')
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, shell=False)
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}, 500

# Additional security measures to mitigate risks
import os
os.environ['PATH'] = '/usr/bin:/bin'  # Restrict PATH environment variable

app.add_middleware(
    SecurityMiddleware,
    force_https=True,
    allowed_hosts=['yourdomain.com'],
)