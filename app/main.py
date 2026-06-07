from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']  # Add more valid hosts as needed
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(request: PingRequest):
    validate_host(request.host)
    subprocess.run(['ping', request.host], check=True)
    return {"status": "completed"}