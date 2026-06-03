from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Sanitize host input to avoid injection attacks
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    # Safer implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}