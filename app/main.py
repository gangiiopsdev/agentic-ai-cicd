from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

def validate_host(host: str) -> bool:
    allowed_hosts = ['127.0.0.1', '::1']  # Add more allowed hosts as needed
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}