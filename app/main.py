from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

async def ping(host: str):
    # Sanitize host input to prevent command injection
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # More restrictive regex check for a valid IP address or hostname
    pattern = r'^[a-zA-Z0-9-_]+$'
    return re.match(pattern, host)

@app.get('/ping')
def ping_route(host: str):
    # Sanitize the host input before using it in subprocess
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}