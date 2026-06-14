from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}

    args = ["ping", host]
    subprocess.call(args)

    return {'status': 'completed'}
def validate_host(host: str) -> bool:
    # Basic validation of the host
    allowed_hosts = ['localhost', '127.0.0.1']  # Example allowed hosts
    return host in allowed_hosts