from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def validate_host(host):
    # Simple example of host validation; replace with more comprehensive checks
    return host.startswith('192.168.') or host == 'localhost'

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    if validate_host(request.host):
        args = ['ping', request.host]
        subprocess.run(args, check=True)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}, 400