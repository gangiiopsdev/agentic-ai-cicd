from fastapi import FastAPI
import subprocess
from typing import Dict, Any

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'localhost']  # Replace with actual validation logic
    return host in allowed_hosts

def safe_ping(host: str) -> Dict[str, Any]:
    if not validate_host(host):
        raise ValueError('Invalid host')
    result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str) -> Dict[str, Any]:
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}