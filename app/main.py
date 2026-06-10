from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation of host input
    if not host or ' ' in host:
        raise ValueError('Invalid host input')
    # Additional validation to ensure the host is a valid IP address
    import ipaddress
    try:
        ipaddress.ip_address(host)
    except ValueError:
        raise ValueError('Invalid host input - must be a valid IP address')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    command = ['ping', host]
    # Use subprocess.run instead of subprocess.call and check the returncode for security
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}