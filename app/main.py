from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host', pre=True)
    def validate_host(cls, v):
        if 'ping' in v.lower():
            raise ValueError('Invalid input')
        return v

@app.get("/ping")
def ping(request: PingRequest):
    args = shlex.split(f'ping {request.host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}