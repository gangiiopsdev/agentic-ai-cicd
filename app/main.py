from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() and not '.' in v:
            raise ValueError('Invalid host format')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    # Use a whitelist of allowed hosts
    allowed_hosts = ['127.0.0.1', 'localhost']
    if request.host not in allowed_hosts:
        raise ValueError('Host not allowed')
    output = subprocess.run(['ping', request.host], capture_output=True, text=True)
    return {"status": "completed", "output": output.stdout}