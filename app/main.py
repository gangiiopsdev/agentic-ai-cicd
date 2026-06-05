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
    safe_host = subprocess.run(['echo', request.host], capture_output=True, text=True).stdout.strip()
    if safe_host not in allowed_hosts:
        raise ValueError(f'Invalid host: {safe_host}')
    subprocess.run(['ping', '-c', '1', safe_host], check=True, shell=False)
    return {'status': 'completed'}