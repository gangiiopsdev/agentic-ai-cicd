from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host
    if not re.match(r'^[a-zA-Z0-9]{1,64}$', host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Add input sanitization
import shlex
def safe_ping(host: str):
    safe_host = shlex.quote(host)
    args = ['ping', safe_host]
    try:
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app.get('/safe-ping')(safe_ping)