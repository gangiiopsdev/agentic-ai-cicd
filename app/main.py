from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def is_valid_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    return host in allowed_hosts

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    if not is_valid_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}

    # Sanitize the input to prevent command injection
    sanitized_host = subprocess.quote(request.host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}