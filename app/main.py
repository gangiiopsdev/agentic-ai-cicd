from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Secure fixed code
app = FastAPI()
def ping_secure(host: str):
    # Validate and sanitize input
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        raise ValueError('Invalid hostname')
    # Use shlex.quote to safely escape arguments
    safe_host = shlex.quote(host)
    result = subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}