from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if 'ping' in v.lower():
            raise ValueError('Invalid input detected in host parameter.')
        return v

app = FastAPI()

@app.post("/ping")
def ping_route(host: PingRequest):
    subprocess.call(['ping', host.host], shell=False)
    return {'status': 'Pong'}