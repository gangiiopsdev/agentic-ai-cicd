from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Ensure the host is a valid IP address or hostname
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Helper function to validate the host input
import re
def validate_host(host: str) -> bool:
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))