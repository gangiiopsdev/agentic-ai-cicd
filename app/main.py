from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
def is_valid_host(host: str):
    # Implement validation logic
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)