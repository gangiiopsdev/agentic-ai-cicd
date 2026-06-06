from fastapi import FastAPI
import subprocess

def ping(host: str):
    try:
        # Validate and sanitize the host input
        if not validate_host(host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}


def validate_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex to match valid IP addresses or hostnames
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None