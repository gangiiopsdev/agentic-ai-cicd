from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run
    if not is_safe_host(host):
        return {'status': 'error', 'output': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def is_safe_host(host: str) -> bool:
    # Implement logic to validate the host
    allowed_hosts = ['127.0.0.1', '::1']
    return host in allowed_hosts