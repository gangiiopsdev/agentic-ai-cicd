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
    if is_valid_host(request.host):
        subprocess.call(['ping', request.host])
    else:
        return {'status': 'invalid host'}
    return {'status': 'completed'}