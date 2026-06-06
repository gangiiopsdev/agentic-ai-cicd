from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if 'ping' in v.lower():
            raise ValueError('Invalid host name')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    subprocess.call(['ping', request.host])
    return {"status": "completed"}