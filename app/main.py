from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}')
        return v

@app.get("/ping")
def ping(host: PingRequest):
    try:
        result = subprocess.run(['ping', host.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}