from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not host or len(host) > 128:
        return {'status': 'invalid_host'}
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid_host'}
    subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get('/ping')
def ping(host: str):  # Use safe_ping instead of direct subprocess call
    result = safe_ping(host)
    return result