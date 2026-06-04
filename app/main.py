from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

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
        # Use regex to validate the host format
        if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
            raise ValueError("Invalid host format")
        result = subprocess.run(['ping', '-c 4', request.host], capture_output=True, text=True, check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "output": str(e)}
    except ValueError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed", "output": result.stdout}