from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '--count=1', re.escape(host)]  # Use re.escape to escape any special characters in the host
    subprocess.run(args, check=True)
    return {'status': 'completed'}
def validate_host(host: str) -> bool:
    # Add validation logic here, e.g., check if the host is in a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts