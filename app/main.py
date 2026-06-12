from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize and quote the host to prevent shell injection
    safe_host = shlex.quote(host)
    subprocess.call(['ping', safe_host])

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    safe_ping(host)
    return {'status': 'completed'}

# Preventive controls:
# - Validate input against expected formats (e.g., IP address, hostname).
def validate_host(host: str) -> bool:
    # Basic validation for IPv4 and domain name
    if host.count('.') == 3 and all(part.isdigit() and int(part) < 256 for part in host.split('.')) or '.' not in host and all(c.isalnum() or c in ['-', '.'] for c in host):
        return True
    return False