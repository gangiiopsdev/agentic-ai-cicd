from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        # Validate and sanitize the host input here
        allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    # Use a whitelist approach to ensure only safe commands are executed
    subprocess.run(['ping', '-c', '1', request.host], check=True)
    return {'status': 'completed'}