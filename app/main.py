from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    # Secure implementation using subprocess.run instead of subprocess.call
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid', 'message': 'Invalid host'}
    return run_ping(host)

def validate_host(host):
    # Add validation logic here to ensure the host is safe to use with subprocess
    import re
    pattern = r'^[a-zA-Z0-9.-_]+$'
    return bool(re.match(pattern, host))