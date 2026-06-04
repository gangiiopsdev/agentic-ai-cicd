from fastapi import FastAPI
import subprocess
from typing import List
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
def is_valid_host(host):
    # Add validation logic for the host here
    return True

app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    if not is_valid_host(request.host):
        return {'status': 'invalid host'}

    try:
        result = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}