from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host: str) -> bool:
    # Implement a simple validation logic here, e.g., check if the host is in a whitelist
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

@app.post('/ping/')
def ping(host: PingRequest):    
    if not validate_host(host.host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}