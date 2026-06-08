from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel
global app
app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host):
    try:
        # Use a whitelist to validate host input
        if not is_valid_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'stdout': result.stdout.decode(), 'stderr': result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

def is_valid_host(host):
    # Implement validation logic here, e.g., checking if the host is in a predefined list
    whitelist = ['127.0.0.1', '::1']  # Example whitelist
    return host in whitelist

@app.post("/ping")
def ping(request: PingRequest):
    return safe_ping(request.host)