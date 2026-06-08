from fastapi import FastAPI
import subprocess
from typing import List
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
def is_valid_host(host: str) -> bool:
    if host in ['localhost', '127.0.0.1'] or (host.startswith('127.') and '.' not in host[3:]) or host == '::1':
        return True
    return False
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    if is_valid_host(request.host):
        try:
            subprocess.run(['ping', '--no-host-decode', request.host], check=True, shell=False)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}