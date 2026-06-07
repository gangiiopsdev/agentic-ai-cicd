from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

def is_valid_host(host: str) -> bool:
    allowed_hosts = ['google.com', 'example.com']  # Example allowed hosts
    return host in allowed_hosts