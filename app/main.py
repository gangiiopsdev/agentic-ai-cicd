from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['localhost', '127.0.0.1']
        if v.strip() not in allowed_hosts:
            raise ValueError("Invalid host")
        return v.strip()

@app.get("/ping")
def ping(host_request: PingRequest):
    subprocess.call(["ping", host_request.host])
    return {"status": "completed"}