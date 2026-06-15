from fastapi import FastAPI
import subprocess
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel, validator

class HostRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum():
            raise ValueError('Invalid host name')
        # Additional validation can be added here, e.g., checking against a whitelist
        return v

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.post('/ping')
def ping(host_request: HostRequest):
    host = host_request.host
    try:
        subprocess.run(['ping', '-c 1', host], check=True)
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed with error code {e.returncode}'}
    return {'status': 'completed'}