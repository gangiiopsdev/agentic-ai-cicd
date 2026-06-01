from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional
def safe_ping(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts

app = FastAPI()

@app.get('/ping')
def ping(host: Optional[str] = None):
    if not host or not safe_ping(host):
        return {'status': 'failed', 'error': 'Host parameter is invalid'}
    try:
        result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}