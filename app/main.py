from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional
import shlex
import os

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    host = request.host
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    if not all(char in allowed_chars for char in host) or '..' in host:
        raise ValueError('Invalid input')

    safe_host = shlex.quote(host)
    command = ['ping', f'-c 1', safe_host]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return {'status': 'completed', 'response': result.stdout}