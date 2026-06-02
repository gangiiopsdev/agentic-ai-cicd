from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

allowed_hosts = ['127.0.0.1', 'localhost']

def safe_ping(host: str):
    if not is_safe_host(host):
        raise Exception('Host is not allowed')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    parsed_url = urlparse(host)
    if parsed_url.scheme or ':' in parsed_url.netloc:
        raise Exception('Invalid host format')
    return safe_ping(host)

def is_safe_host(host: str):
    for allowed_host in allowed_hosts:
        if host == allowed_host or host.startswith(allowed_host + '.'):  # Add additional checks as needed
            return True
    return False