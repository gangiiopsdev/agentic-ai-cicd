from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only specific hosts or ranges
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

@app.post('/ping')
def ping_secure(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = shlex.split(f'ping {request.host}')
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}