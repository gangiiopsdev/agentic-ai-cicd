from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def ping(host: str):
    # Ensure the host is safe to avoid command injection
    if not host.strip().isdigit():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}