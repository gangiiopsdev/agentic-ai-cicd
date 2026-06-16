from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    allowed_hosts = ['example.com', 'example.org']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    try:
        validate_host(request.host)
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}