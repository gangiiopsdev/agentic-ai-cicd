from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

class HostRequest(BaseModel):
    host: str

def execute_ping(host: str):
    try:
        command = ['ping', '-c 1', host]
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}

app = FastAPI()

@app.post('/ping')
def ping(request: HostRequest):
    try:
        validate_host(host=request.host)
    except ValueError as e:
        return {'status': 'error', 'output': str(e)}
    return execute_ping(host)

def validate_host(host: str):
    if not host.isalnum() or len(host) > 50:
        raise ValueError('Invalid hostname')