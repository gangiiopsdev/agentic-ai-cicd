from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.startswith('localhost') and not v.startswith('127.0.0.1'):
            raise ValueError('Invalid host')
        return v

@app.get("/ping")
def ping(request: PingRequest):\n    subprocess.run(['ping', request.host], check=True)\n    return {"status": "completed"}