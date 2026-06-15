from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '.-')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Enhanced input validation to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    try:
        output = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}