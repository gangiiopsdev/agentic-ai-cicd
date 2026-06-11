from fastapi import FastAPI
import subprocess
from typing import Optional
import re
def sanitize_input(input_str: str) -> str:
    allowed_chars = r'^[a-zA-Z0-9.-]+$'
    return ''.join(filter(lambda char: char in allowed_chars, input_str))

app = FastAPI()

@app.get('/ping')
def ping(host: Optional[str] = None):    # Simple regex to validate host input
    if not host:
        return {'status': 'failed', 'error': 'Host is required'}
    sanitized_host = sanitize_input(host)
    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}