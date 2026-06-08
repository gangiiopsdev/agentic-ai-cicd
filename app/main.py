from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize host input to avoid injection attacks
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    # Safer implementation using subprocess.run with shell=False
    result = subprocess.run(['/bin/ping', '-c', '4', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'stdout': result.stdout}