from fastapi import FastAPI
import subprocess
from typing import Optional
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    # Regex pattern for allowed IP addresses
    ip_pattern = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
    return re.match(ip_pattern, host) is not None

def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': str(e)}

@app.get("/ping")
def ping_route(host: str):
    # Validate and sanitize input to prevent injection attacks
    if not validate_host(host):
        return {'status': 'error', 'error': 'Invalid host'}
    return ping(host)