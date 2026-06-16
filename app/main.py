from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel
global allowed_hosts
allowed_hosts = ['localhost', '127.0.0.1']

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    global allowed_hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    validate_host(request.host)
    args = ['ping', '--count=1'] + shlex.split(request.host)
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}