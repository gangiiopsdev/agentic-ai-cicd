from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not isinstance(host, str) or len(host.strip()) == 0:
        return {'status': 'failed', 'output': 'Invalid host input'}
    # Validate the host input to prevent command injection
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None:
        return {'status': 'failed', 'output': 'Invalid host input'}
    # Sanitize the host input to prevent command injection
    sanitized_host = subprocess.quote(host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}