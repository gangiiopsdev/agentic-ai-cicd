from fastapi import FastAPI
import subprocess
from shlex import quote

def sanitize_host(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host")
    return host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        sanitized_host = quote(sanitize_host(host))
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}