from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'localhost']  # Replace with actual allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    try:
        output = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {
            "status": "completed",
            "output": output.stdout,
            "host": request.host
        }
    except subprocess.CalledProcessError as e:
        return {
            "status": "failed",
            "error": str(e),
            "host": request.host
        }