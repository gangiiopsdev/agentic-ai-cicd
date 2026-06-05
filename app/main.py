from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
        if v not in allowed_hosts:
            raise ValueError('Invalid host format')

@app.get("/ping")
def ping(request: PingRequest):
    try:
        subprocess.run(['ping', f'-c 1 {request.host}'], check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}