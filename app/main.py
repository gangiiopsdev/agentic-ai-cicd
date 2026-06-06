from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it is safe
    if not validate_host(host):
        return {'status': 'failed', 'reason': 'Invalid host'}, 400

    # Secure implementation
    subprocess.run(['ping', '-c', '1', '--no-hostnames', host], check=True, shell=False)

    return {'status': 'completed'}
def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., check for allowed hosts or patterns
    allowed_hosts = ['127.0.0.1', '::1']  # Example of allowed hosts
    return host in allowed_hosts