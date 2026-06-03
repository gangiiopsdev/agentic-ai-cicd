from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    allowed_hosts = ['example.com', 'test.com']  # Add your list of allowed hosts here
    if not request.host in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {shlex.quote(request.host)}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}