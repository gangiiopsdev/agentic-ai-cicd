from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'error', 'message': 'Invalid host name'}
    # Secure implementation using subprocess.run without shell=True
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}