from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host: str):
    # Validate and sanitize input here if necessary
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout, 'returncode': result.returncode}

def is_valid_host(host: str) -> bool:
    # Simple validation example
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts

@app.post("/ping")
def ping(request: PingRequest):
    result = safe_ping(request.host)
    return result