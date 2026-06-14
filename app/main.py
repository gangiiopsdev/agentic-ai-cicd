from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with proper input sanitization
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '--', host]  # Use '--' to prevent command injection
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def validate_host(host: str) -> bool:
    # Add validation logic here to ensure the host is safe
    allowed_hosts = ['example.com', 'localhost']  # Example list of allowed hosts
    return host in allowed_hosts