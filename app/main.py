from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    host = request.host
    # Sanitize input to prevent command injection
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}

# Example of a simple validation function
def is_valid_host(host: str) -> bool:
    allowed_hosts = ['localhost', '127.0.0.1']  # Add more valid hosts as needed
    return host in allowed_hosts