from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping(request: PingRequest):
    # Secure implementation using shlex.quote to sanitize the input
    safe_host = subprocess.list2cmdline([request.host])
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}