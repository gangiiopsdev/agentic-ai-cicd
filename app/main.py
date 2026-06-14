from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        raise ValueError('Invalid host')
    # Secure implementation
    subprocess.run(['ping', request.host], check=True)
    return {"status": "completed"}