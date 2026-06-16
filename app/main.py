from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}, 400

    # Use a whitelist of allowed hosts or use an allowed list for the command
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'error': 'Host not allowed'}, 403

    subprocess.run(['ping', host], check=True)

    return {'status': 'completed'}