from fastapi import FastAPI
import subprocess
from typing import Optional
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

def sanitize_input(input_str: str) -> str:
    # Sanitize input to prevent injection attacks
    sanitized = subprocess.list2cmdline([input_str])
    return sanitized

@app.get('/ping')
def ping(host: str):  # Simple regex to validate host input
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run([sanitize_input('ping'), '-c', '1', sanitize_input(host)], check=True, capture_output=True, text=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}