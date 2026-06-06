from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

app = FastAPI()

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not v.isalnum() or len(v) > 64:
            raise ValueError('Invalid host name')
        return v

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    args = shlex.split(f'ping {shlex.quote(request.host)}')
    try:
        subprocess.run(args, check=True, timeout=5)  # Add a timeout to prevent denial of service
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}