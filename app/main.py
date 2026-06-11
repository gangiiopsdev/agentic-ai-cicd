from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate host input before running subprocess
    if not validate_host(host):
        raise ValueError('Invalid host input')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}
def validate_host(host: str) -> bool:
    # Implement validation logic here
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts