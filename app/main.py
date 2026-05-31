from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str
def validate_host(host):
    # Allow only alphanumeric characters and periods
    return re.match(r'^[a-zA-Z0-9.]+$', host) is not None
@app.post("/ping")
def ping(request: PingRequest):
    if not validate_host(request.host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', request.host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
# Preventive controls:
# 1. Validate and sanitize user input.
# 2. Avoid using shell=True if not necessary.
# 3. Use safer alternatives like ping3 or similar libraries.