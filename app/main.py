from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    allowed_hosts = ['example.com', '127.0.0.1']  # Add more allowed hosts as needed
    if request.host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    try:
        output = subprocess.check_output(['ping', request.host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()} 
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.output.decode()}