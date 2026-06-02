from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import ipaddress

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    try:
        ip_address = ipaddress.ip_address(host)
        return True
    except ValueError:
        return False

@app.post('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'error', 'message': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': f'Ping failed: {e}'}, 500