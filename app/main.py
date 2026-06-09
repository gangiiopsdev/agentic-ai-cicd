from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
        if not all(char in allowed_chars for char in v):
            raise ValueError('Invalid characters in host')

@app.post('/ping')
def ping(request: PingRequest):
    # Use a whitelist of allowed hosts or restrict the input further
    if request.host in ['allowed_host1', 'allowed_host2']:
        subprocess.run(['ping', '-c 1', request.host], check=True)
    return {'status': 'completed'}