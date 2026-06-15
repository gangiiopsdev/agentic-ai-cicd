from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingResponse(BaseModel):
    status: str

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    try:
        # Use full path for 'ping' command to mitigate potential issues
        result = subprocess.run(['usr/bin/ping', sanitized_host], capture_output=True, text=True, check=True)
        return PingResponse(status=result.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status=e.stderr)

# Sanitize input before using it in subprocess
def sanitize_input(input_str: str) -> str:
    sanitized = ''.join(filter(str.isalnum, input_str))
    return sanitized

import os

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host')
    sanitized_host = sanitize_input(host)
    try:
        # Use full path for 'ping' command to mitigate potential issues
        result = subprocess.run(['usr/bin/ping', sanitized_host], capture_output=True, text=True, check=True)
        return PingResponse(status=result.stdout)
    except subprocess.CalledProcessError as e:
        return PingResponse(status=e.stderr)

def is_safe_host(host: str) -> bool:
    # Implement logic to check if the host is safe
    allowed_hosts = ['safe1.com', 'safe2.com']
    return host in allowed_hosts