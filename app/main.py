from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional
import shlex
def is_allowed_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.example.com']
    return host in allowed_hosts

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    if not is_allowed_host(request.host):
        return {'status': 'error', 'message': 'Host not allowed'}
    safe_host = shlex.quote(request.host)
    args = ['ping', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}