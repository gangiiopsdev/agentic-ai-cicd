from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Add more allowed hosts as needed
    if host not in allowed_hosts:
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if validate_host(host) and validate_ip_address(host):
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

import ipaddress
def validate_ip_address(ip_str):  # Helper function to validate IP address format
    try:
        ipaddress.ip_address(ip_str)
        return True
    except ValueError:
        return False