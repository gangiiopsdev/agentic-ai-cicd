from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    # Simple validation: allow only alphanumeric characters and hyphens
    return host.isalnum() or '-' in host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        # Use subprocess with shell=False and a whitelist of allowed hosts
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}