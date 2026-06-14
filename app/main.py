from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # Define a whitelist of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {"status": "failed", "error": "Invalid host"}
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}