from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class HostValidator:
    @validator('host')
    def validate_host(cls, value):
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
        if not all(char in allowed_chars for char in value):
            raise ValueError('Invalid characters in host name')
        return value

@app.get('/ping', dependencies=[Depends(HostValidator)])
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, text=True, capture_output=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}