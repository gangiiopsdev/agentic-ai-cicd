from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def safe_ping(host: str) -> str:
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str) -> dict:
    if not validate_host(host):
        return {'error': 'Invalid host'}
    return {'result': safe_ping(host)}

def validate_host(host: str) -> bool:
    # Add validation logic to ensure the host is trusted
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    return host in allowed_hosts