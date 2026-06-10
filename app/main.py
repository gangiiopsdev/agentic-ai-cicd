from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def validate_host(host: str):
    # Add validation logic to ensure the host is safe
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts