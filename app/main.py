from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate the host to ensure it is a valid IP address or domain name
    if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', re.escape(request.host)], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}