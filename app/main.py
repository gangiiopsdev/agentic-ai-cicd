from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input
    if not host or len(host) > 255 or '.' not in host:
        raise ValueError('Invalid host input')
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Host contains invalid characters')
    # Sanitize input by escaping special characters
    sanitized_host = subprocess.quote(host)
    args = ['ping', '-c', '1', '--', sanitized_host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}