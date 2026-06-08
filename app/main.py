from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingCommand:
    def __init__(self, host):
        self.host = host

    @validator('host', pre=True)
    def validate_host(cls, v):
        allowed_hosts = ['8.8.8.8', '127.0.0.1']
        if v not in allowed_hosts:
            raise ValueError(f'Host {v} is not allowed')
        return v

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    ping_command = PingCommand(host)
    output = ping_command.execute()
    return {'status': 'completed', 'output': output}