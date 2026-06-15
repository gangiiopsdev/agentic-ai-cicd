from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    try:
        # Validate the host input to ensure it is a valid IP address or hostname
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host'}
        # Use a whitelist of allowed hosts/IPs instead of regex for more robust validation
        allowed_hosts = ['127.0.0.1', '::1']  # Example list, customize as needed
        if host not in allowed_hosts:
            return {'status': 'failed', 'error': 'Host not allowed'}
        subprocess.run(['ping', '-c 1', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize and validate the host input further
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'failed', 'error': 'Invalid host'}
    allowed_hosts = ['127.0.0.1', '::1']  # Example list, customize as needed
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    subprocess.run(['ping', '-c 1', host], check=True)
    return {'status': 'completed'}