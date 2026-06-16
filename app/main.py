from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def is_safe_host(host):
    # Simple example of checking if the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get("/ping")
def ping(request: PingRequest):
    if not is_safe_host(request.host):
        raise ValueError('Unsafe host')
    # Secure implementation
    subprocess.call(['ping', request.host])
    return {"status": "completed"}