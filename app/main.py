from fastapi import FastAPI
import subprocess
from typing import List
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation
    try:
        if request.host == 'localhost' or request.host.startswith('127.0.0.1'):
            subprocess.run(['ping', '--no-host-decode', request.host], check=True, shell=False)
        else:
            return {'status': 'failed', 'error': 'Invalid host'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}