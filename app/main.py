from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel, validator

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def check_host(cls, v):
        allowed_hosts = ['example.com', 'another-example.com']  # Define a list of allowed hosts
        if v not in allowed_hosts:
            raise ValueError('Host not allowed')
        return v

app = FastAPI()

@app.post('/ping')
def ping(request: PingRequest):
    try:
        args = shlex.split(f'ping -c 4 {request.host}')  # Use '-c 4' to limit the number of pings
        output = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}