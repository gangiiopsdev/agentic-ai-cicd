from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    # Further validation and sanitization of the host input
    allowed_hosts = ['example.com', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Host not allowed')
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}

# Function to validate the host input
def is_valid_host(host: str) -> bool:
    # Enhanced validation logic (e.g., check for allowed domains, IPs, etc.)
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None