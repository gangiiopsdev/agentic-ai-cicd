from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional

app = FastAPI()

@app.get('/ping')
def ping(host: Optional[str] = None):
    allowed_hosts = ['127.0.0.1', 'localhost']  # Example whitelist
    if not host or host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host parameter is required or invalid'}
    try:
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}