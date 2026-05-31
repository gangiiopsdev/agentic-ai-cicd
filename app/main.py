from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

def is_safe_host(host):
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual allowed hosts
    return host in allowed_hosts

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    if not is_safe_host(request.host):
        return {"status": "error", "message": "Invalid host"}
    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    return {"status": "completed", "output": result.stdout}