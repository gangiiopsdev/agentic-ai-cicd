from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def check_host(cls, v):
        if not v.startswith('192.168.'):
            raise ValueError('Only IP addresses in the 192.168.x range are allowed')
        return v

@app.get('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    # Use a safer method to check if the host is within the allowed range
    if not request.host.startswith('192.168.'):
        raise ValueError('Only IP addresses in the 192.168.x range are allowed')
    args = shlex.split(f'ping -c 4 {request.host}')  # Limit to 4 pings for security
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}