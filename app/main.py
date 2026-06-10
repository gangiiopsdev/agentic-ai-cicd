from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with full path and input sanitization
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    result = subprocess.run(['/sbin/ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}