from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safer implementation using subprocess.run with validation
    if not host.isdigit():
        raise ValueError('Invalid host')
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout, 'stderr': result.stderr}