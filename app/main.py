from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host provided"}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}

@validator('host')
def validate_host(host: str):
    allowed_hosts = ['example.com', 'another-example.com']  # List of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')