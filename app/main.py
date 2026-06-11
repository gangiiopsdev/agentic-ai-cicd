from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host: str) -> bool:
    # Simple regex to allow only alphanumeric characters and a few special characters
    return re.match(r'^[a-zA-Z0-9.-]{1,}$', host) is not None

@app.get("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        output = subprocess.check_output(['ping', '-c', '1', request.host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {"status": "failed", "error": str(e)}