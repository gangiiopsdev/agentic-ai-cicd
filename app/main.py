from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

class PingRequest(BaseModel):
    host: str

def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Replace request.host with a safe, hardcoded value for demonstration purposes
        result = subprocess.run(['ping', '-c', '1', 'localhost'], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()