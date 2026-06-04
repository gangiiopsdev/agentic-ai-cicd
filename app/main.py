from fastapi import FastAPI
import subprocess
from pydantic import validator, BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['127.0.0.1', '::1']  # Add other allowed hosts as needed
        if v not in allowed_hosts:
            raise ValueError('Invalid host')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}