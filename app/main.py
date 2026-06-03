from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        # Validate and sanitize the host input
        if not cls.is_valid_host(v):
            raise ValueError('Invalid or untrusted host input')
        return v

    @staticmethod
def is_valid_host(host):
        # Implement validation logic here (e.g., allowed domains)
        return '.' in host

@app.get("/ping")
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}