from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        # Use a more secure and dynamic approach for allowed hosts
        if not cls.is_valid_host(v):
            raise ValueError(f'Invalid host {v}. Only specific hosts are allowed.')

    @classmethod
def is_valid_host(cls, host):
        import socket
        try:
            socket.gethostbyname(host)
            return True
        except socket.gaierror:
            return False

@app.get('/ping')
def ping(request: PingRequest):
    allowed_hosts = ['127.0.0.1', '::1']  # Specify a list of allowed hosts
    if request.host not in allowed_hosts:
        raise ValueError(f'Invalid host {request.host}. Only specific hosts are allowed.')
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}