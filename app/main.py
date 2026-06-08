from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    safe_host = sanitize_host(host)
    ping_safe(safe_host)
    return {'status': 'completed'}

def is_valid_host(host: str):
    # Add logic to validate the host input
    return True

def sanitize_host(host: str):
    # Sanitize the host input to prevent injection vulnerabilities
    import re
    allowed_chars = re.compile(r'^[a-zA-Z0-9.-]+$')
    if not allowed_chars.match(host):
        raise ValueError('Invalid characters in host')
    return host