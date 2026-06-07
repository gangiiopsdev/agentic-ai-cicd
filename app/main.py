from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

def is_valid_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

class PingRequest(BaseModel):
    host: str

def safe_ping(host):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    if not is_valid_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}

    return safe_ping(request.host)