from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def is_valid_host(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    return host in allowed_hosts

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    if is_valid_host(request.host):
        args = ['ping', '-c', '1', request.host]
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    else:
        return {"status": "error", "message": "Invalid host"}