from fastapi import FastAPI
import subprocess
from typing import Optional
def safe_ping(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

def sanitize_host(host: str) -> str:
    # Sanitize the host input to prevent command injection
    return ''.join(c for c in host if c.isalnum() or c in '.-')

app = FastAPI()

@app.get('/ping')
def ping(host: Optional[str] = None):
    if not host or not safe_ping(host):
        return {'status': 'failed', 'error': 'Host parameter is invalid'}
    try:
        sanitized_host = sanitize_host(host)
        result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}