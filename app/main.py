from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return False
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'output': 'Invalid host input'}
    # Sanitize the host input to prevent command injection
    sanitized_host = subprocess.quote(host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}