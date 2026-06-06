from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isdigit():
            raise ValueError('Host must be a valid IP address or hostname')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    args = shlex.split(f'ping {request.host}')
    subprocess.run(args, check=True, capture_output=True)

    return {'status': 'completed'}