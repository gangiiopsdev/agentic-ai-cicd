from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

class HostRequest(BaseModel):
    host: str

def execute_ping(host: str):
    try:
        output = subprocess.check_output(['ping', '-c 1', host], stderr=subprocess.STDOUT, shell=False)
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

import shlex

def safe_execute(command: list[str]):
    try:
        output = subprocess.check_output(shlex.split(' '.join(command)), stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.output.decode('utf-8')}

@app.post('/ping_safe')
def ping_safe(request: HostRequest):
    try:
        validate_host(host=request.host)
    except ValueError as e:
        return {'status': 'error', 'output': str(e)}
    command = ['ping', '-c 1', request.host]
    return safe_execute(command)