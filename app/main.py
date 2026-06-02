from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run with validation and sanitization
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}