from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host):
    return host.replace(';', '').replace('&', '').replace('|', '')

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid command injection
    sanitized_host = sanitize_host(host)
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'status': 'failed', 'error': 'Invalid hostname'}

    try:
        result = subprocess.run(['ping', '-c', '1', sanitized_host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}