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
    subprocess.run(['ping', request.host], check=True)
    return {'status': 'completed'}