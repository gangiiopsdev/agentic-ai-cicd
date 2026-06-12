from fastapi import FastAPI
import subprocess
import re
def safe_ping(host: str):
    allowed_hosts = ['google.com', 'example.com']
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        raise ValueError('Host not allowed')
    try:
        result = subprocess.run(['/usr/bin/ping', '--count=1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):  # Input validation should be done here
    try:
        result = safe_ping(host)
        return result
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}