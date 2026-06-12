from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    host = request.host
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host) or '..' in host:
        raise ValueError('Invalid input')

    # Sanitize the hostname to prevent command injection
    sanitized_host = subprocess.list2cmdline([host])
    result = subprocess.run(['ping', '-c 1', sanitized_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {'status': 'completed', 'response': result.stdout}