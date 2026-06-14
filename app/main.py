from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping(request: PingRequest):
    # Use a whitelist of allowed hosts instead of sanitizing input
    allowed_hosts = ['example.com', 'localhost']
    if request.host in allowed_hosts:
        try:
            result = subprocess.run(['ping', request.host], check=True, capture_output=True, text=True)
            return {"status": "completed", "output": result.stdout}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "error": str(e)}
    else:
        return {"status": "failed", "error": "Host not allowed"}