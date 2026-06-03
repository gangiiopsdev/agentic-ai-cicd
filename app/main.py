from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input before using it in the subprocess call
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}
def is_valid_host(host: str) -> bool:
    # Implement validation logic for the host input
    allowed_hosts = ['example.com', 'test.com']  # Example allowed hosts
    return host in allowed_hosts