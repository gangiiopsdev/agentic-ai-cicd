from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError('Invalid host name')
    return host.strip().lower()

def validate_ip_address(ip):
    import ipaddress
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not validate_ip_address(sanitized_host):
        raise ValueError('Invalid IP address')
    args = shlex.split(f'ping {sanitized_host}')
    subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed'}