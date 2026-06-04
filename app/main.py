from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

globally_safe_hosts = ['127.0.0.1', '::1']  # List of safe hosts

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    @validator('host', pre=True)
    def validate_host(cls, v):
        if v not in globally_safe_hosts:
            raise ValueError('Unauthorized host')
        return v

    subprocess.run(['ping', *shlex.split(v)], check=True, capture_output=True)
    return {'status': 'completed'}