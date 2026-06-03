from fastapi import FastAPI
import subprocess
import socket

app = FastAPI()

def safe_ping(host: str):
    # Validate input
    try:
        socket.gethostbyname(host)
    except socket.gaierror:
        raise ValueError("Invalid host")
    
    # Use a whitelist of allowed hosts or use a more secure method
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        raise ValueError("Host is not allowed")
    
    # Use platform-independent library for network operations
    import urllib.request
    try:
        urllib.request.urlopen(f'http://{host}/ping').getcode()
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            raise ValueError("Host is not reachable")
        else:
            raise ValueError(str(e))
    
@app.get("/ping")
def ping(host: str):
    return safe_ping(host)