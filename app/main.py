from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

def safe_ping(host: str):
    # Validate the host input to prevent injection attacks
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(c in valid_chars for c in host):
        raise ValueError('Invalid hostname')
    # Use subprocess.run instead of subprocess.call and avoid using shell=True
    result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return result.stdout

@app.get('/ping')
def ping(host: str):
    try:
        output = safe_ping(host)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}