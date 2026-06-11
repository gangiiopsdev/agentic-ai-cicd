from fastapi import FastAPI
import subprocess
import re
def safe_ping(host):
    # Validate the host to ensure it's a trusted IP or domain
    if is_trusted_host(host):
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    else:
        raise ValueError('Untrusted host')
def is_trusted_host(host):
    # Implement your validation logic here, e.g., allow only specific IPs/domains
    trusted_hosts = ['127.0.0.1', 'localhost']
    return host in trusted_hosts or re.match(r'^[a-zA-Z0-9.-]+$', host)
global app = FastAPI()
@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}