from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not validate_host(host):
        raise ValueError('Invalid host input')
    args = ['ping', shlex.quote(host)]  # Use shlex.quote to sanitize the host input
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

def validate_host(host: str) -> bool:
    # Implement validation logic here (e.g., regex check for valid IP or hostname)
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None