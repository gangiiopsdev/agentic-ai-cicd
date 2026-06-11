from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

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
    args = shlex.split(f'ping {request.host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}