from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host):
    # Enhanced validation to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]{1,}$', host):
        return {'status': 'invalid', 'message': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'invalid', 'message': 'Invalid host name'}
    return safe_ping(host)