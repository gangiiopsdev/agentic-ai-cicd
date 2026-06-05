from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

# Define a whitelist of allowed host names
ALLOWED_HOSTS = {'example.com', 'test.com'}

def is_valid_host(host: str):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None and host in ALLOWED_HOSTS

@app.get('/ping')
def ping_endpoint(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}