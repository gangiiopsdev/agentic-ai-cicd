from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import socket

def validate_host(host):
    try:
        socket.gethostbyname(host)
        return True
    except socket.gaierror:
        return False

app = FastAPI()
class PingRequest(BaseModel):
    host: str

def execute_ping(host):
    command = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed: {e}'}, 500

def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'error', 'message': 'Invalid host input'}
    return execute_ping(request.host)

@app.post('/ping', response_model=BaseModel)
def ping_request(request: PingRequest):
    return ping(request)