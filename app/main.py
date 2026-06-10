from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'error': str(e.stderr.decode())}

@app.get("/ping")
def ping_endpoint(host: Optional[str] = None):
    if host is None:
        return {'error': 'Host parameter is required'}
    # Validate input to prevent security issues
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'error': 'Invalid host parameter'}
    return ping(host)