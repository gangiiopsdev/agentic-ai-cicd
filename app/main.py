from fastapi import FastAPI
import subprocess
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    args = ['ping', '-c', '1', host]
    try:
        result = subprocess.run(args, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': str(e)}
    return {'status': 'completed', 'output': result.stdout}
def is_valid_host(host: str) -> bool:
    allowed_hosts = ['google.com', 'example.com']  # Example allowed hosts
    return host in allowed_hosts