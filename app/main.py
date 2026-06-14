from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Validate and sanitize host input
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Use a whitelist of allowed hosts or network ranges
    allowed_hosts = ['192.168.1.0/24', '10.0.0.0/8']
    if any(host.startswith(allowed_host) for allowed_host in allowed_hosts):
        subprocess.run(['ping', host], check=True, shell=False)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Invalid host range'}

def is_valid_host(host: str) -> bool:
    # Simple validation logic, replace with more robust checks
    return '.' in host and len(host.split('.')) == 4

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)