from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
        if v not in allowed_hosts:
            raise ValueError(f'Invalid host: {v}')
        return v

@app.get('/ping')
def ping(request: PingRequest):
    subprocess.run(['ping', request.host], check=True)
    return {'status': 'completed'}