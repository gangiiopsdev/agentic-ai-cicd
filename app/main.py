from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        allowed_hosts = ['example.com', 'test.com']  # Replace with actual allowed hosts
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping')
def ping(request: PingRequest):
    # Safe way to call ping using a safe command
    command = ['ping', '-c', str(1), request.host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}